import simpy

class NodoConvergecast:
    def __init__(self, id_nodo, valor, hijos, padre, canal_entrada, canal_salida):
        '''Inicializamos el nodo con su ID, valor, hijos, padre y los canales de comunicación.'''
        self.id_nodo = id_nodo
        self.valor = valor
        self.hijos = hijos  # Lista de IDs de los hijos
        self.padre = padre  # ID del nodo padre
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.val_set = set()  # Conjunto de valores consolidados

    def convergecast(self, env):
        '''Algoritmo que implementa la consolidación de valores en un árbol.'''
        
        # Si el nodo es una hoja (no tiene hijos)
        if not self.hijos:
            # Enviamos nuestro valor al nodo padre
            print(f"Tiempo {env.now}: Hoja {self.id_nodo} envía valor ({self.id_nodo}, {self.valor}) a su padre {self.padre}")
            self.canal_salida.envia((self.id_nodo, self.valor), self.padre)
        else:
            # Si no somos hoja, esperamos los mensajes de todos nuestros hijos
            recibidos = []
            while len(recibidos) < len(self.hijos):
                mensaje = yield self.canal_entrada.get()
                print(f"Tiempo {env.now}: Nodo {self.id_nodo} recibió {mensaje} de su hijo.")
                recibidos.append(mensaje)
            
            # Consolidamos los valores recibidos de los hijos
            self.val_set = set(recibidos) | {(self.id_nodo, self.valor)}
            print(f"Tiempo {env.now}: Nodo {self.id_nodo} consolidó valores {self.val_set}")
            
            # Si no somos la raíz, enviamos la información consolidada al padre
            if self.padre != self.id_nodo:
                print(f"Tiempo {env.now}: Nodo {self.id_nodo} envía valores consolidados a su padre {self.padre}")
                self.canal_salida.envia(self.val_set, self.padre)
            else:
                # Si somos la raíz, computamos la función final
                print(f"Tiempo {env.now}: Raíz {self.id_nodo} ha recibido todos los valores y computa la función.")
                self.computar_funcion_final(self.val_set)

    def computar_funcion_final(self, val_set):
        '''Computa una función sobre el conjunto de valores finales en la raíz.'''
        resultado = sum(valor for _, valor in val_set)  # Ejemplo: suma de los valores
        print(f"El resultado final en la raíz {self.id_nodo} es: {resultado}")
