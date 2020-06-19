heuristic={}
class Graph(object):
    """
    A simple undirected, weighted graph
    """

    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def astar(graph, initial_node, goal_node, h):
    global heuristic
    closed_set = set()  # set of nodes already evaluated
    nodes = set()  # set of tentative nodes to be evaluated
    nodes.add(initial_node)

    visited = {}  # map of navigated nodes
    g_score = {initial_node: 0}  # distance from start along optimal path
    h_score = heuristic  # heuristic estimate
    f_score = {initial_node: h_score[initial_node]}  # estimated dist

    while nodes:
        x = None
        for node in nodes:
            if x is None:
                x = node
            elif f_score[node] < f_score[x]:
                x = node

        nodes.remove(x)
        if x == goal_node:
            return visited

        closed_set.add(x)
        for y in graph.edges[x]:
            if y in closed_set:
                continue
            tentative_g_score = g_score[x] + graph.distances[(x, y)]

            flag = False
            if y not in nodes or tentative_g_score < g_score[y]:
                nodes.add(y)
                flag = True

            if flag:
                visited[y] = x

                g_score[y] = tentative_g_score

                f_score[y] = g_score[y] + h_score[y]

    return False


def shortest_path(graph, initial_node, goal_node, h):
    paths = astar(graph, initial_node, goal_node, h)
    route = [goal_node]

    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()

    return route


def start():

    import math
    global heuristic
    sldist = lambda c1, c2: math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)
    g = Graph()
    nodes=int(input("enter number of nodes"))
    print("enter nodes in co-ordinate format with heuristic value and spaces in between")
    for i in range(0,nodes):
        x = list(input().split())
        x = [int(i) for i in x]
        g.add_node((x[0], x[1]))
        heuristic[(x[0],x[1])]=x[2]
    for i in g.nodes:
        conn=int(input("enter number of nodes connected to"+str(i)))
        for j in range(0,conn):
             y=list(input("enter co-ordinates of node connected to"+str(i)+" and path length").split())
             y = [int(i) for i in y]
             g.add_edge(i, (y[0],y[1]), y[2])
    z=list(input("enter start node and end with co-ordinates separted by spaces").split())
    z=[int(i) for i in z]
    string=""
    route=shortest_path(g, (z[0], z[1]), (z[2], z[3]), sldist)
    for i in route:
        string=string+"-->"+str(i)
    print(string)
   # g.distances[((0, 0), (1, 1))] = 2
    #g.distances[((1, 1), (0, 0))] = 2

#    assert shortest_path(g, (0, 0), (2, 2), sldist) == [(0, 0), (1, 0), (2, 2)]

 #   g.distances[((0, 0), (1, 0))] = 1.3
  #  g.distances[((1, 0), (0, 0))] = 1.3

    #print( shortest_path(g, (0, 0), (2, 2), sldist) == [(0, 0), (0, 1), (2, 2)])
