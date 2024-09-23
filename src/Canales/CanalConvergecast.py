import simpy
from Canales.Canal import Canal

class CanalConvergecast(Canal):
    '''Simula un canal de comunicación entre nodos.'''
    def __init__(self, env):
        self.env = env
        self.cola = simpy.Store(env)

    def envia(self, mensaje, destino):
        '''Envia un mensaje al nodo destino.'''
        print(f"Tiempo {self.env.now}: Mensaje {mensaje} enviado a {destino}")
        # En una implementación completa, enviaríamos el mensaje al canal_entrada del nodo destino
        self.cola.put(mensaje)
