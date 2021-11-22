import numpy as np

def floydWarshall(G):
  n = len(G)

  cost = [[float('inf')]*n for _ in range(n)]
  path = [[-1]*n for _ in range(n)]

  for u in range(n):
    cost[u][u] = 0
    for v, w in G[u]:
      cost[u][v] = w
      path[u][v] = u

  for k in range(n):
    for i in range(n):
      if i == k: continue
      for j in range(n):
        if i == j or j == k: continue
        f = cost[i][k] + cost[k][j]
        if f < cost[i][j]:
          cost[i][j] = f
          path[i][j] = path[k][j]

  return path, cost
