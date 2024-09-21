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
        for vecino_id in vecinos:
            canal_vecino = self.canales[vecino_id]
            print(f"Tiempo {self.env.now}: Enviando mensaje '{mensaje}' a Nodo {vecino_id}")
            canal_vecino.put(mensaje)

