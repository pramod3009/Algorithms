def dfs(adjLists, s,goal):
    stack = []
    stack.append(s)
    n = len(adjLists)
    visited = []
    for i in range(0, n):
        visited.append(False)
    x=""
    while (len(stack) > 0):
        v = stack.pop()
        if (not visited[v]):
            visited[v] = True
            x=x+"-->"+str(v)
            if v==goal:
                return x
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            # alternatively: iterate through the adjacency list in reverse order
            # but this is only to get the same output as the recursive dfs
            # otherwise, this would not be necessary
            stack_aux = []
            for w in adjLists[v]:
                if (not visited[w]):
                    stack_aux.append(w)
            while (len(stack_aux) > 0):
                stack.append(stack_aux.pop())
def start(x):
  graph = [[1, 2],  [3,4], [5,6], [7,8], [9,10 ], [11,12],[13,14], [],  [],  [],[16],[15],[],[],[],[],[]]


  return dfs(graph,0,x)


