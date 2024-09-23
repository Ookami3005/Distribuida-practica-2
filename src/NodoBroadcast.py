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
            vamos a enviar un mensaje a todos los demás nodos.

            - Si el nodo tiene un mensaje inicial (`self.mensaje` no es `None`), se considera el nodo distinguido y envía el mensaje a todos sus vecinos.
            - Si el nodo no tiene un mensaje inicial, espera a recibir un mensaje en su canal de entrada.
            - Al recibir un mensaje, lo reenvía a todos sus vecinos excepto al nodo del cual recibió el mensaje, evitando ciclos innecesarios.    
        '''
        
        if self.mensaje is not None:
            # Nodo distinguido inicia el broadcast
            print(f"Tiempo {env.now}: Nodo {self.get_id()} envía mensaje '{self.mensaje}' a sus vecinos")
            self.canal_salida.envia((self.get_id(), self.mensaje), self.vecinos)
        else:
            while True:
                mensaje = yield self.canal_entrada.get()
                print(f"Tiempo {env.now}: Nodo {self.get_id()} recibió mensaje '{mensaje[1]}' del nodo {mensaje[0]}")
                if self.mensaje is None:
                    self.mensaje = mensaje[1]  # Actualizar el mensaje del nodo con el mensaje recibido
                    for vecino_id in self.vecinos:
                        if vecino_id != mensaje[0]:
                            print(f"Tiempo {env.now}: Nodo {self.get_id()} reenvía mensaje '{mensaje[1]}' a Nodo {vecino_id}")
                            self.canal_salida.envia(mensaje, [vecino_id])