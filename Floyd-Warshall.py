import numpy as np

def pseudoFloydWarshall(graph):

  n = len(graph)
  gain = np.zeros((n, n))
  for i in range(n):
    gain[i, i] = 1
    for j in range(n):
      gain[i, j] = graph[i, j]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        gain[i, j] = max(gain[i, j], gain[i, k] * gain[k, j])
        
  return gain
