from Canales.CanalBroadcast import *
from NodoBroadcast import *


# Las unidades de tiempo que les daremos a las pruebas
TIEMPO_DE_EJECUCION = 50


class TestPractica1:
    ''' Clase para las pruebas unitarias de la práctica 1. '''
    # Las aristas de adyacencias de la gráfica.
    adyacencias = [[1, 2], [0, 3], [0, 3, 5], [1, 2, 4], [3, 5], [2, 4]]

    # Aristas de adyacencias del árbol
    adyacencias_arbol = [[1, 2], [3], [5], [4], [], []]

    

    # Prueba para el algoritmo de Broadcast.
    def test_ejercicio_tres(self):
        ''' Prueba para el algoritmo de Broadcast. '''
        # Creamos el ambiente y el objeto Canal
        env = simpy.Environment()
        bc_pipe = CanalBroadcast(env)
        # La lista que representa la gráfica
        grafica = []

        # Creamos los nodos
        for i in range(len(self.adyacencias)):
            grafica.append(NodoBroadcast(i, [], bc_pipe.crea_canal_de_entrada(), bc_pipe))

        # Actualizamos la lista de vecinos con referencias a objetos nodo
        for i, nodo in enumerate(grafica):
            nodo.vecinos = [grafica[j] for j in self.adyacencias_arbol[i]]

        # Asignar mensaje inicial al nodo distinguido (nodo 0)
        grafica[0].mensaje = "Hola, soy el nodo distinguido"

        # Le decimos al ambiente lo que va a procesar ...
        for nodo in grafica:
            env.process(nodo.broadcast(env))
        # ...y lo corremos
        env.run(until=TIEMPO_DE_EJECUCION)

        # Probamos que todos los nodos tengan ya el mensaje
        mensaje_enviado = grafica[0].mensaje
        for nodo in grafica:
            assert mensaje_enviado == nodo.mensaje, (
                'El nodo %d no tiene el mensaje correcto' % nodo.id_nodo)

