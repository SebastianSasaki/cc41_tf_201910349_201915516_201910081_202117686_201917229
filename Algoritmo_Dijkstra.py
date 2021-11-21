def get_ls(st, dp, n):
  ls = []
  locals = []
  for y in range(n): 
    for x in range(n): 
      tp = 0      
      if [x,y] in st:
        tp = 1        
      if [x,y] in dp:
        tp = 2
      ls.append(adjacents(x, y, n))
      locals.append(tp)
  return ls, locals


def toListWithCosts(G):
  new_list = []
  for c in G:
    l = []
    for n in c:
      l.append((n,1))
    new_list.append(l)
  return new_list


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
