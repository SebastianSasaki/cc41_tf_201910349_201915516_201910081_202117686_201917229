def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost


# Analisaremos el algoritmo Dijkstra, tambien llamado "Algoritmo de caminos minimos" y veremos su efectividad que tendria en la aplicación del grafo final.

# El Algoritmo de Dijkstra tiene una notación O(V^2) por lo que me da a entender que mientras vertices tenga el grafo más sera su notación. Y que el tiempo de ejecución sera más
# grande mientras más grande sea el grafo.
# Vertices: 1000000. Notación Algoritmo Dijkstra: O(1000000^2). Y tenemos que tener en cuenta que se repetira 60 veces, 1 por cada almacen que hay. Todo esto hace que este
# algoritmo no sea una solución tan óptima.
