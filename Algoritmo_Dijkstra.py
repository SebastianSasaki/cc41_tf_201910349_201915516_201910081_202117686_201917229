def dijkstra(G, L, s):
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

  min_path = [None]*n
  for i, v in enumerate(L):
      if v == 2:
        min_path[i] = path[i]
        m = path[i]
        while m != s:          
          min_path[m] = path[m]
          m = path[m]

  return min_path, cost
