import bfs
import dfs
import astardynamic
import djikstra
def start():
    print("enter choice 1.bfs 2.dfs 3.uniform cost search 4.astart")
    x=input()
    if x=="1":
        graph={}
        print("enter number  nodes")
        nodes=int(input())
        for i in range(0,nodes):
            print("enter nodes connected to node with spaces:"+str(i))
            x=list(input().split())
            x = [int(i) for i in x]
            graph[i]=x
        goal=int(input("enter goal state"))
        print('bfs ' +bfs.bfs(graph,0,goal))
    if x=="2":
        graph=[]
        print("enter number  nodes")
        nodes = int(input())
        for i in range(0, nodes):
            print("enter nodes connected to node with spaces:" + str(i))
            x = list(input().split())
            x = [int(i) for i in x]
            graph.append(x)
        goal = int(input("enter goal state"))
        print(dfs.dfs(graph, 0,goal))
    if x=="3":
        djikstra.start1()

    if x=="4":
        astardynamic.start()







