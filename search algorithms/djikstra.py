import heapq
import sys


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {}  # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start:  # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            smallest = heapq.heappop(nodes)[1]  # Vertex in nodes with smallest distance in distances
            if smallest == finish:  # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]:  # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize:  # All remaining vertices are inaccessible from source
                break

            for neighbor in self.vertices[smallest]:  # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor]  # Alternative path distance
                if alt < distances[neighbor]:  # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def __str__(self):
        return str(self.vertices)

def start(a,b):
    g = Graph()

    y={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
    z={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
    g.add_vertex('A', {'B': 7, 'C': 8})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    x=g.shortest_path(z[a], z[b])
    x=x[::-1]
    s=str(a)
    for i in x:
        s=s+"-->"+str(y[i])
    return(s)
def start1():
    g=Graph()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets = list(alphabets)
    y={}
    z={}
    for i in range(0,26):
        y[alphabets[i]]=i
        z[i]=alphabets[i]
    nodes=int(input("enter number of nodes"))
    for i in range(0,nodes):
        conn=int(input(("enter number nodes connected to "+str(i))))
        edges={}
        for j in range(0,conn):
            print("cost from"+str(i)+"to")
            x=list(input().split())
            x=[int(a1) for a1 in x]
            edges[z[x[0]]]=x[1]
        g.add_vertex(z[i],edges)
    start1=int(input("enter start state"))
    goal=int(input("enter goal state"))
    x = g.shortest_path(z[start1], z[goal])
    x = x[::-1]
    s = str(start1)
    for i in x:
        s = s + "-->" + str(y[i])
    print(s)