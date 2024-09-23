Integrantes:

-Del Monte Ortega Maryam Michelle 320083527

Explicación de Algoritmos:

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


