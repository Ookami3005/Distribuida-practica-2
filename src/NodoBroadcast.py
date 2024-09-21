import simpy
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1

class NodoBroadcast(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, mensaje=None):
        super().__init__(id_nodo, vecinos, canal_entrada, canal_salida)
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.mensaje = mensaje

    def broadcast(self, env):
        ''' Algoritmo de Broadcast. Desde el nodo distinguido (0)
            vamos a enviar un mensaje a todos los demás nodos.'''
        
        if self.mensaje is not None:
            # Nodo distinguido inicia el broadcast
            print(f"Tiempo {env.now}: Nodo {self.id_nodo} envía mensaje '{self.mensaje}' a sus vecinos")
            self.canal_salida.envia((self.id_nodo, self.mensaje), self.vecinos)
        else:
            while True:
                mensaje = yield self.canal_entrada.get()
                print(f"Tiempo {env.now}: Nodo {self.id_nodo} recibió mensaje '{mensaje[1]}' del nodo {mensaje[0]}")
                if self.mensaje is None:
                    self.mensaje = mensaje[1]  # Actualizar el mensaje del nodo con el mensaje recibido
                    for vecino in self.vecinos:
                        if vecino.get_id() != mensaje[0]:
                            print(f"Tiempo {env.now}: Nodo {self.id_nodo} reenvía mensaje '{mensaje[1]}' a Nodo {vecino.get_id()}")
                            self.canal_salida.envia(mensaje, [vecino])