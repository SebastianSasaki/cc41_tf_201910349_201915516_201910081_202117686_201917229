# Espacio de búsqueda
El problema de este trabajo es llamado VRP (Vehicle Routing Problem), para poder hallar su espacio de busqueda tenemos como punto de partida cualquiera de los puntos de
distribución que en este caso son entre 50 a 100 opciones disponibles. Se busca un balance entre costo de entrega y tiempo de distribución. Por lo que nosotros inferimos
que la ruta más optima sería empezar por los puntos de entrega que están más cerca del punto de distribución de partida y luego seguir con los puntos de entrega que están más
lejos.

Estado Inicial:
- El estado inicial del espacio de busqueda de este problema son los puntos de distribución que estan repartidos por toda la ciudad. No existen 2 puntos en una misma coordenada, ya sean puntos iguales o uno de entrega y el otro de distribución.

Estado Final:
- El estado final del esapcio de busqueda es el mismo punto que el estado inicial, solo que con todo el recorrido ya realizado. Una vez que llegue al ultimo nodo del recorrido, tiene que regresar al punto de inicio de manera directa.

Reglas:
- Un punto de distribución será la partida y la llegada, pero durante su recorrido no puede pasar más de una vez por un mismo punto.

Soluciones:
- Existen algoritmos que nos permiten resolver de manera eficaz esa problemática, tales como BFS, DFS, Dijkstra, entre otros.


![img_VRP](https://cdn.discordapp.com/attachments/847950429839949884/892793809119879189/vrpgs_solution.png)
