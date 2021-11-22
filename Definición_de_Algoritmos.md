# Algoritmo 1

Topic | Desc
-|-
Autor | Hugo Quispe
Técnica principal | Algoritmo Bellman-Ford

# Algoritmo de Bellman Ford

El algoritmo de Bellman-Ford es una buena opción para generar el camino mas corto en un grafo dirigido ponderado, una de las ventajas de este algoritmo es que acepta caminos que pueden ser negativos. La semejanza que comparte con el algoritmo Disjkstra es la manera de ser implementada pero lo que los diferencia que tienen estos algoritmos es que Disjkstra requiere que los pesos de las aristas no tienen que ser negativas. Por lo que el Algoritmo Bellman-Ford normalmente se utiliza cuando hay aristas con peso negativo, pero puede ser utilizado si no los contiene. Este algoritmo fue desarrollado por Richard Bellman, Samuel End y Lester Ford.

![img_VRP](https://media.geeksforgeeks.org/wp-content/uploads/bellmanford2.png)

# Algoritmo 2

Topic | Desc
-|-
Autor | Sebastián Sasaki
Técnica principal | Algoritmo Dijkstra

# Algoritmo Dijkstra

Para poder resolver este problema, el algoritmo que yo usaría sería el algoritmo de Dijkstra o también conocido algoritmo UCS.La idea subyacente en este algoritmo consiste en ir explorando todos los caminos más cortos que parten del vértice origen y que llevan a todos los demás vértices; cuando se obtiene el camino más corto desde el vértice origen hasta el resto de los vértices que componen el grafo, el algoritmo se detiene. Se trata de una especialización de la búsqueda de costo uniforme y, como tal, no funciona en grafos con aristas de coste negativo (al elegir siempre el nodo con distancia menor, pueden quedar excluidos de la búsqueda nodos que en próximas iteraciones bajarían el costo general del camino al pasar por una arista con costo negativo).

Este algoritmo sería la solución ya que permite recorrer un grafo siguiendo la ruta más económica posible, esto significa que ve el peso de la arista que une dos nodos y recorre el que menos peso tenga. Pero este algoritmo necesita algunos cambios para que pueda resolver nuestro problema al 100%. El algoritmo debe reconocer que no puede pasar por el mismo punto de entrega dos veces, esto se puede hacer con un condicional "if" que indique que, si un punto ya ha sido visitado, no lo puede visitar otra vez. También se agregará variables extras para recopilar información sobre el recorrido. Cantidad recorrida, tiempo demorado, etc.
En el análisis asintótico, la complejidad del algoritmo dijkstra es de O(n2), o "n elevado al cuadrado".

![img_VRP](https://4.bp.blogspot.com/-pRAitO3ivd4/U58qJJh_4JI/AAAAAAAAAWY/Wfxr7s-_u64/s1600/Incanato+dijsktra+recorrido.JPG)

# Algoritmo 3

Topic | Desc
-|-
Autor | Sebastián Gonzales
Técnica principal | Algoritmo BFS

# Algoritmo BFS

Es un algoritmo de búsqueda no informada utilizado para recorrer o buscar elementos en un grafo (usado frecuentemente sobre árboles). Intuitivamente, se comienza en la raíz (eligiendo algún nodo como elemento raíz en el caso de un grafo) y se exploran todos los vecinos de este nodo. A continuación para cada uno de los vecinos se exploran sus respectivos vecinos adyacentes, y así hasta que se recorra todo el árbol.

El algoritmo BFS consiste en los siguientes pasos:

1) Dado un vértice fuente s, BFS sistemáticamente explora los vértices de G para “descubrir” todos los vértices alcanzables desde s.
2) Calcula la distancia (menor número de vértices) desde s a todos los vértices alcanzables.
3) Después produce un árbol BF con raíz en s y que contiene a todos los vértices alcanzables.

![image](https://user-images.githubusercontent.com/67605232/142799598-86886259-68f6-4355-a44d-79b98f41b3e3.png)



# Algoritmo 4

Topic | Desc
-|-
Autor | Jorge Sanchez Vallejos
Técnica principal | Algoritmo Floyd-Warshall

# Algoritmo de Floyd-Warshall

El agoritmo de FLoyd-Warshall, descrito en 1959 por Bernard Roy, es una opción muy utilizada cuando se desea determinar el camino mínimo entre todos los los pares de nodos de un grafo, mediante comparaciones entre los posibles caminos logra mejorar gradualmente la estimación hasta llegar a la más óptima. La adaptación de este algoritmo permitiría la resolución del problema de enrutamineto de vehículos. 

Sea un grafo G con conjunto de vértices V, numerados de 1 a N. Sea además una función **caminoMinimo(i,j,k)** que devuelve el camino mínimo de i a j usando únicamente los vértices de 1 a k como puntos intermedios en el camino. Ahora, dada esta función, nuestro objetivo es encontrar el camino mínimo desde cada i a cada j usando únicamente los vértices de 1 hasta k+1.

Hay dos candidatos para este camino: un camino mínimo, que utiliza únicamente los vértices del conjunto (1...k); o bien existe un camino que va desde i hasta k+1, y de k+1 hasta j, que es mejor. Sabemos que el camino óptimo de i a j que únicamente utiliza los vértices de 1 hasta k está definido por **caminoMinimo(i,j,k)**, y está claro que si hubiera un camino mejor de i a k+1 a j, la longitud de este camino sería la concatenación del camino mínimo de i a k+1 (utilizando vértices de  (1...k) ) y el camino mínimo de k+1 a j (que también utiliza los vértices en  (1...k) ).

La fórmula del agoritmo es:

>**caminoMinimo(i,j,k) = min(caminoMinimo(i,j,k-1), caminoMinimo(i,k,k-1) + caminoMinimo(k,j,k-1));**

>**caminoMinimo(i,j,0) = pesoArista(i,j);**

Aquí evidenciamos que se puede implementar de forma recursiva, pero al reconocer que esto tiene un límite, en grafos más densos sería más eficiente trabajar con pilas (stacks).

La notación asintótica de este algoritmo se estima ser: **O(v3)**
![img_VRP](http://2.bp.blogspot.com/-zNImYywGBWw/VkVDmgna0rI/AAAAAAAAAMw/laDiXGr2HUI/s1600/Sin%2Bt%25C3%25ADtulo.png)

# Algoritmo 5

Topic | Desc
-|-
Autor | Jhonel Rios
Técnica principal | Algoritmo de Prim

# Algoritmo de Prim

El algoritmo de Prim se encarga de encontrar el camino mínimo dentro de un grafo conexo y no dirigido. El resultado del algoritmo es un árbol de expansión mínima; es decir, un árbol formado por todos los vértices de dicho gráfo.

**Funcionamiento**

1. Se escoge cualquier vértice del grafo. Este será el vértice de partida del árbol.
2. Se escoge la arista de menor tamaño que conecta al vértice actual con el siguiente y lo agregamos al árbol.
3. Se repite el paso 2 mientras que existan vértices que no estén visitados y asegurandose que no formen ningún ciclo.

**Complejidad**

Al tratarse de dos ciclos for anidados, la complejidad de este algortimo es de O(n^2).

![img_Prim](https://cmop17.files.wordpress.com/2009/08/prim.png?w=600)
