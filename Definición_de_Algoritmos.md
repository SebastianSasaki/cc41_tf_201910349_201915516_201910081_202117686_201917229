# Algoritmo 1

Topic | Desc
-|-
Autor | Hugo Quispe
Técnica principal | Algoritmo K-opt

# Algoritmo k-Opt

El algoritmo Or-opt es considerado como la versión reducida del algoritmo "3-opt", implementado por Or en 1976.
Este algoritmo consiste en eliminar una secuencia de k clientes presentados en la ruta y colocarlos en otra posición dentro de la ruta, de tal manera que permanezcan en secuencia y conservar el mismo orden. Una aplicación sería que primero se realice los movimientos cuando el valor de k es 3, luego cuando vale 2 y finalmente cuando toma el valor de 1. Como se muestra en la imagen la ruta y todas las posibles maneras de reubicar a los tres primeros nodos de manera que define Or-opt. Además, Según Aarts y Lenstra en el año 2003 el tiempo obtenido al ejecutar el 2-opt se producirá el peor caso de los casos con un tamaño de tour menor al 5% sobre la HKLB, pero al optimizar el tiempo de la heurística 3-opt tendrá un tour del 3% sobre la HKLB.
La complejidad que obtiene al considerar el peor de los casos es de O(log2(n)).

![img_VRP](https://www.researchgate.net/publication/297660097/figure/fig1/AS:341517492342784@1458435523017/The-2-opt-and-or-opt-operations.png)

# Algoritmo 2

Topic | Desc
-|-
Autor | Sebastián Sasaki
Técnica principal | Algoritmo Dijkstra

# Algoritmo Dijkstra

Para poder resolver este problema, el algoritmo que yo usaría sería el algoritmo de Dijkstra o también conocido algoritmo UCS. Que tiene esta forma estándar(python):

def dijkstra(G, s):                  # T(n) =
  
  n = len(G)                         # 2
  
  visited = [False]*n                # 1 + n
  
  path = [None]*n                    # 1 + n
  
  cost = [math.inf]*n                # 1 + n
  
  cost[s] = 0                        # 2
  
  queue = [(0, s)]                   # 1
  
  while queue                        # 1  
    
    g_u, u = hq.heappop(queue)       #   2
    
    if not visite[u]:                #   2 +
      
      visited[u] = True              #     2 
      
      for v, w in G[u]:              #     n *
        
        f = g_u + w                  #       2
        
        if f < cost[v]:              #       1 + 
          
          cost[v] = f                #         2
          
          path[v] = u                #         2
          
          hq.heappush(queue, (f, v)) #         1
  return path, cost                  

Este algoritmo sería la solución ya que permite recorrer un grafo siguiendo la ruta más económica posible, esto significa que ve el peso de la arista que une dos nodos y recorre el que menos peso tenga. Pero este algoritmo necesita algunos cambios para que pueda resolver nuestro problema al 100%. El algoritmo debe reconocer que no puede pasar por el mismo punto de entrega dos veces, esto se puede hacer con un condicional "if" que indique que, si un punto ya ha sido visitado, no lo puede visitar otra vez. También se agregará variables extras para recopilar información sobre el recorrido. Cantidad recorrida, tiempo demorado, etc.
En el análisis asintótico, la complejidad del algoritmo dijkstra es de O(n2), o "n elevado al cuadrado".
