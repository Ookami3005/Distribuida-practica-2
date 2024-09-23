import simpy
from Nodo import *
from Canales.CanalBroadcast import *

TICK = 1

class NodoGenerador(Nodo):
    '''Implementa la interfaz de Nodo para el algoritmo de flooding.'''
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida

        # Atributos propios del algoritmo
        self.padre = None if id_nodo != 0 else id_nodo # Si es el nodo distinguido, el padre es el mismo
        self.hijos = list()
        self.mensajes_esperados = len(vecinos) # Cantidad de mensajes que esperamos

    def genera_arbol(self, env):
        #Tu código aquí
        if self.id_nodo == 0:
            self.canal_salida.envia((self.id_nodo, 'GO'), self.vecinos)
            return

        while True:
            mensaje = yield self.canal_entrada.get()
            remitente, bandera = mensaje
            if bandera == 'GO':
                if self.padre is None:
                    self.padre = remitente
                    if self.mensajes_esperados == 0:
                        self.canal_salida.envia((self.id_nodo, True), [v for v in self.vecinos if v.id_nodo == remitente])
                    else:
                        self.canal_salida.envia((self.id_nodo, 'GO'), [vecino for vecino in self.vecinos if vecino.id_nodo != remitente])
                else:
                    self.canal_salida.envia((self.id_nodo, False), [v for v in self.vecinos if v.id_nodo == remitente])
            else:
                self.mensajes_esperados -= 1
                if bandera: self.hijos.append(remitente)
                if self.mensajes_esperados == 0:
                    if self.padre != self.id_nodo:
                        self.canal_salida.envia((self.id_nodo, True), [v for v in self.vecinos if v.id_nodo == self.padre])