Integrantes:

-Del Monte Ortega Maryam Michelle 320083527
-Monroy Romero Sahara Mariel 320206391
- Romero Cruz Fernando 319314256

Explicación de Algoritmos:


** NodoVecinos: 

Este algoritmo para conocer a los vecinos de los vecinos en una red sigue un enfoque colaborativo entre los nodos. Cada nodo comienza enviando a sus vecinos la lista de sus propios vecinos. Luego, a medida que 
los nodos reciben estas listas, actualizan su conjunto de identificadores, lo que les permite expandir su conocimiento más allá de sus conexiones inmediatas. Este intercambio de información puede continuar opcionalmente, 
permitiendo una mayor difusión y actualización de las listas de vecinos en la red. A través de esta interacción, cada nodo termina con un conjunto completo que incluye no solo a sus vecinos directos, sino también a los vecinos de estos. 

** NodoGenerador

Esta función busca hallar un árbol generador a través de los nodos del sistema. Partiendo desde el nodo distinguido, se envia la bandera GO a sus nodos hijos,
de modo que puedan reconocerlo como su padre y repetir este mismo proceso. Si algún nodo recibe un 'GO' cuando ya ha reconocido a su padre, entonces envía
una bandera negativa al nodo remitente, indicando que ya posee un padre. Una vez que los nodos han recibido todos los mensajes que esperan, es decir, los
de sus vecinos, entonces devuelve una bandera positiva a su padre. Cualquier nodo que reciba esta bandera positiva, reconoce a dicho nodo como uno de sus hijos.

** BroadCast:

Esta función simula cómo un mensaje se propaga desde un nodo inicial (nodo distinguido) a través de toda la red.

1. El nodo distinguido es aquel que inicia el proceso de difusión. En este caso, es el nodo con un mensaje inicial (self.mensaje no es "None").
   - Si el nodo es el nodo distinguido, inmediatamente envía el mensaje a todos sus vecinos. Esto se logra utilizando el método "envia" del canal de salida ("self.canal_salida"), que distribuye el mensaje a los canales de entrada de los nodos vecinos.

2. Si el nodo no tiene un mensaje inicial, entra en un ciclo de espera activa, utilizando "yield self.canal_entrada.get()", que bloquea el proceso hasta que recibe un mensaje.
   -Al recibir un mensaje, el nodo:
     - Imprime un mensaje en la consola indicando la recepción, el contenido del mensaje, y el nodo emisor.
     - Si el nodo aún no ha recibido ningún mensaje previamente ("self.mensaje" es "None"), actualiza su estado interno para reflejar que ha recibido el mensaje.
     - Reenvía el mensaje a todos sus vecinos, excepto al nodo del cual lo recibió. Esto se hace para evitar enviar el mensaje de regreso al nodo emisor, lo que podría causar redundancia o ciclos.

3. Al reenviar el mensaje, el nodo verifica que no lo envía de vuelta al nodo del cual lo recibió (verifica que el ID del vecino sea diferente al del nodo emisor).

** Convergecast:

El algoritmo implementa Convergecast en un árbol, donde cada nodo tiene un valor y debe enviar ese valor hacia su nodo padre. Si el nodo es una hoja (no tiene hijos), envía su valor 
inmediatamente al padre. Los nodos intermedios, que no son hojas ni la raíz, esperan recibir los valores de todos sus hijos, los consolidan junto con su propio valor y 
luego envían el conjunto consolidado al padre. Finalmente, la raíz, una vez que recibe todos los valores consolidados, ejecuta una función (en este caso, la suma de los valores) para obtener el resultado final. 
El algoritmo simula la comunicación entre nodos utilizando canales de entrada y salida.

