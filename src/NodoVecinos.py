import simpy
from Nodo import *
from Canales.CanalBroadcast import *

class NodoVecinos(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de conocer a los vecinos de tus vecinos.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo con su id, lista de vecinos, y los canales de comunicación.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.identifiers = set()  # Conjunto donde guardaremos los vecinos de los vecinos
        self.identifiers.update(vecinos)  # Añadimos los propios vecinos

    def conoceVecinos(self, env):
        ''' Algoritmo que hace que el nodo conozca a los vecinos de sus vecinos.
            Lo guarda en la variable identifiers.'''
        
        # Enviamos la lista de nuestros vecinos a nuestros vecinos
        print(f"Tiempo {env.now}: Nodo {self.id_nodo} envía sus vecinos {self.vecinos} a sus vecinos.")
        self.canal_salida.envia(self.vecinos, self.vecinos)
        
        # Esperamos y recibimos mensajes de nuestros vecinos
        while True:
            mensaje = yield self.canal_entrada.get()
            print(f"Tiempo {env.now}: Nodo {self.id_nodo} recibió lista de vecinos {mensaje}.")

            # Actualizamos la lista de identificadores con los vecinos recibidos
            self.identifiers.update(mensaje)
            
            # Opción de enviar nuevamente a los vecinos la nueva información que se ha obtenido (opcional para propagar más información)
            print(f"Tiempo {env.now}: Nodo {self.id_nodo} ahora conoce los vecinos {self.identifiers}.")
