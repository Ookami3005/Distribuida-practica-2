import simpy

class Nodo:
    """Representa un nodo.

    Cada nodo tiene un id, una lista de vecinos y dos canales de comunicación.
    Los métodos que tiene son únicamente getters.
    """
    def __init__(self, id_nodo: int, vecinos: list, canal_entrada: simpy.Store,
                 canal_salida: simpy.Store):
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida

    """
    Método de acceso del identificador de un nodo
    """
    def get_id(self) -> int: return self.id

    """
    Método de acceso a la lista de vecinos del nodo
    """
    def get_vecinos(self) -> list: return self.vecinos

    """
    Método de acceso al canal de entrada del nodo
    """
    def get_canal_entrada(self) -> simpy.Store: return self.canal_entrada

    """
    Método de acceso al canal de salida del nodo
    """
    def get_canal_salida(self) -> simpy.Store: return self.canal_salida
