def bellmanFord(G, s):
  n = len(G)

  # initialize
  cost = [float('inf')]*n
  cost[s] = 0
  path = [-1]*n

  # relax
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u] + w
          path[v] = u

  # check negative cycle
  for u in range(n):
    for v, w in G[u]:
      if cost[u] + w < cost[v]:
        return None, None

  return path, cost
