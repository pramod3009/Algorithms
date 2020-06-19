

def bfs(graph,start,goal, path=[]):
  q=[start]
  s=""
  while q:
    v=q.pop(0)  #THIS WILL DELETE FROM FRONT FROM 0th position hence will act as a queue
    if not v in path:
      s=s+"-->"+str(v)
      path=path+[v]
      q=q+graph[v]
      if v==goal:
        return s


def start(x):
  graph = {0:[1, 2],1:[3,4],2:[5,6],3:[7,8],4:[9,10 ],5:[11,12],6:[13,14],7:[],8:[],9:[],10:[16],11:[15],12:[],13:[],14:[],15:[],16:[]}

  return 'bfs '+bfs(graph,0, x)

