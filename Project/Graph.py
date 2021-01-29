from math import *

class Graph:

    def __init__(self, size):
        self.arr = [[0 for i in range(size)] for j in range(size)]
        self.edges = 0
        self.size=size
        self.distance = []
        self.source = None
        self.travel = []

    def has_vertex(self, index):
       if index >= self.size:
           return False
       return True

    def copy_graph(self):
        graph = Graph(self.size)
        graph.edges = self.edges
        for i in range(graph.size):
            for j in range(graph.size):
                graph.arr[i][j]=self.arr[i][j]
        return graph

    def complement_graph(self):
        graph = Graph(size)
        graph.edges = self.edges
        for i in range(graph.size):
            for j in range(graph.size):
                if self.arr[i][j]==0 and self.arr[j][i]==0 and i!=j:
                    graph.arr[i][j]=1
                    graph.arr[j][i]=1
        return graph


    def is_in_range(self,v1,v2):
        if(v1 > self.size - 1 or v2 > self.size - 1 or v1 < 0 or v2 < 0):
            return False
        return True

    def has_edge(self, v1, v2):
        if not self.is_in_range(v1,v2):
            return -1
        else:
            return self.arr[v1][v2]!=0

    def weight_edge(self, v1, v2):
        if self.has_edge(v1,v2):
            return self.arr[v1][v2]
        else:
            print("Edge doesn't exist!")
            return -1

    def add_edge(self,v1,v2,value):
        if (value<=0):
            print("Edge value can not be negative!")
            return -1
        if self.has_edge(v1, v2) is not False:
            print ("Edge already exists or indexes are outside of range! ",v1,"-",v2)
            return -2
        self.arr[v1][v2]=value
        self.arr[v2][v1]=value
        self.edges+=1

    def remove_edge(self,v1,v2):
        if (self.edges == 0):
            print("No edges to remove")
            return -1
        if self.has_edge (v1, v2) is not True:
            print("Edge doesn't exist or indexes outside of range! ",v1,"-",v2)
            return -2
        self.arr[v1][v2] = 0
        self.arr[v2][v1] = 0
        self.edges-=1

    def remove_vertex(self, index):
        if self.has_vertex(index) is not True:
            print("Vertex ", index, "doesn't exist")
            return -1
        for i in range(self.size):
            if(self.arr[i][index]!=0):
                self.edges-=1
                self.arr[i][index]=0
                if (self.arr[index][i] != 0):
                    self.edges -= 1
                    self.arr[index][i]=0

    def print_graph(self):
        print("Graph structure")
        for i in range(self.size):
            for j in range(self.size):
                print (self.arr[i][j], end = " ")
            print(" ")

    def print_edges(self):
        print("Existing edges and their values")
        for i in range(self.size):
            for j in range(i,self.size):
                if(self.arr[i][j]>0):
                    print(i,"<--->",j, " | ", self.arr[i][j])

    def min_distance(self, visited, key):
        minKey = inf
        index = -1
        for i in range(self.size):
            if visited[i]==False and minKey>key[i]:
                minKey=key[i]
                index=i
        return index

    def dijkstra(self,source):
        visited = [False]*self.size
        self.source=source
        self.distance = [inf]*self.size
        self.distance[source]=0
        self.travel = [None] * self.size
        for i in range(self.size):
            u = self.min_distance(visited, self.distance)
            visited[u]=True
            for v in range(self.size):
                if(self.arr[u][v]>0):
                    if visited[v]==False:
                        newDistance = self.distance[u]+self.arr[u][v]
                        if(newDistance<self.distance[v]):
                            self.distance[v]=newDistance
                            self.travel[v]=u
        print(("Vertex     Distance from source"))
        for i in range (0,self.size):
            print('{0:4d} {1:16.0f}'.format(i,self.distance[i]))

        print("Paths taken to get to each vertex")
        for i in range(0,self.size):
            if(self.travel[i]!=None):
                path = []
                curr=self.travel[i]
                while(curr!=None and curr!=self.source):
                    path.append(curr)
                    if(self.travel[curr]==None):
                        curr=self.source
                    else:
                        curr=self.travel[curr]
                if(len(path)!=0):
                    print(self.source,end =" ")
                    for j in range(len(path)):
                        print(" - ", path[j],end=" ")
                    print(" - ",i)
                else:
                    print(self.source," - ", i)
            else:
                if (i == self.source):
                    print(self.source)
                else:
                    print("Could not get to vertex ", i)