import simpy
from Canales.Canal import Canal

class CanalBroadcast(Canal):
    '''
    Clase que modela un canal, permite enviar mensajes one-to-many.
    '''

    def __init__(self, env, capacidad=simpy.core.Infinity):
        super().__init__(env, capacidad)
        self.env = env
        self.capacidad = capacidad
        self.canales = []

    def crea_canal_de_entrada(self):
        '''
        Creamos un canal de entrada.
        '''
        canal_entrada = simpy.Store(self.env, capacity=self.capacidad)
        self.canales.append(canal_entrada)
        return canal_entrada

    def envia(self, mensaje, vecinos):
        '''
        Envia un mensaje a los canales de entrada de los vecinos.
        '''
        for vecino in vecinos:
            print(f"Tiempo {self.env.now}: Enviando mensaje '{mensaje[1]}' a Nodo {vecino.get_id()}")
            vecino.canal_entrada.put(mensaje)
