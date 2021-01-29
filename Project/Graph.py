from math import *
maxGraph = 100

class Graph:

    def __init__(self):
        self.arr = [[0 for i in range(maxGraph)] for j in range(maxGraph)]  # or [] if matrix is supposed to be dynamic
        self.vertices = 0
        self.edges = 0


    def is_full(self):
        return self.vertices==maxGraph;

    def is_empty(self):
        return self.vertices==0

    def add_vertex(self):
        if self.is_full()==True:
            raise IndexError("Matrix is full!")   # Alternative: print("Matrix is full!") else:
        self.vertices+=1                             # If matrix size is supposed to be dynamic instead of static
                                                     # Add a column by looping through all rows and add a row
    def has_vertex(self, index):
       if index >= self.vertices:
           return False
       return True

    def copy_graph(self):
        graph = Graph()
        graph.vertices = self.vertices
        graph.edges = self.edges
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                graph.arr[i][j]=self.arr[i][j]
        return graph

    def complement_graph(self):
        graph = Graph()
        graph.vertices = self.vertices
        graph.edges = self.edges
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                if self.arr[i][j]==0 and self.arr[j][i]==0 and i!=j:
                    graph.arr[i][j]=1
                    graph.arr[j][i]=1
        return graph


    def is_in_range(self,v1,v2):
        if(v1 > self.vertices - 1 or v2 > self.vertices - 1 or v1 < 0 or v2 < 0):
            return False
        return True

    def has_edge(self, v1, v2):
        if(self.is_in_range(v1,v2)==False):
            return -1
        else:
            return (self.arr[v1][v2]!=0) == True

    def weight_edge(self, v1, v2):
        if self.has_edge(v1,v2):
            return self.arr[v1][v2]
        else:
            print("Edge doesn't exist!")
            return -1

    def add_edge(self,v1,v2,value):
        if (value<0):
            print("Edge value can not be negative!")
            return -1
        if(self.has_edge(v1, v2)!=False):
            print ("Edge already exists or indexes are outside of range! ",v1,"-",v2)
            return -2
        self.arr[v1][v2]=value
        self.arr[v2][v1]=value
        self.edges+=1

    def remove_edge(self,v1,v2):
        if (self.edges == 0):
            print("No edges to remove")
            return -1
        if(self.has_edge (v1, v2)!=True):
            print("Edge doesn't exist or indexes outside of range! ",v1,"-",v2)
            return -2
        self.arr[v1][v2] = 0
        self.arr[v2][v1] = 0
        self.edges-=1

    def remove_vertex(self,index):
        if self.is_empty()== True:
            print("No vertices to remove")
            return -1
        if self.has_vertex(index)==False:
            print("Vertex ", index, "doesn't exist")
            return -2
        for i in range(index):
            self.arr[i][index] = 0
            for j in range(index+1,self.vertices):
                self.arr[i][j-1]=self.arr[i][j]
        for i in range(index+1,self.vertices):
            for j in range(index):
                self.arr[i-1][j] = self.arr[i][j]
            for j in range(index+1,self.vertices):
                self.arr[i-1][j-1]=self.arr[i][j]
        self.vertices-=1


    def print_graph(self):
        print("Graph structure")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print (self.arr[i][j], end = " ")
            print(" ")

    def print_edges(self):
        print("Existing edges and their values")
        for i in range(self.vertices):
            for j in range(i,self.vertices):
                if(self.arr[i][j]>0):
                    print(i,"<--->",j, " | ", self.arr[i][j])

    def min_distance(self, visited, key):
        minKey = inf
        index = -1
        for i in range(self.vertices):
            if visited[i]==False and minKey>key[i]:
                minKey=key[i]
                index=i
        return index

    def dijkstra(self,source):
        visited = [False]*self.vertices
        distance = [inf]*self.vertices
        distance[source]=0
        travel = [None] * self.vertices
        for i in range(self.vertices):
            u = self.min_distance(visited, distance)
            visited[u]=True
            for v in range(self.vertices):
                if(self.arr[u][v]>0):
                    if visited[v]==False:
                        newDistance = distance[u]+self.arr[u][v]
                        if(newDistance<distance[v]):
                            distance[v]=newDistance
                            travel[v]=u
        print(("Vertex     Distance from source"))
        for i in range (0,self.vertices):
            print('{0:4d} {1:16d}'.format(i,distance[i]))

        print("Paths taken to get to each vertex")
        for i in range(0,self.vertices):
            if(travel[i]!=None):
                path = []
                curr=travel[i]
                while(curr!=None and curr!=source):
                    path.append(curr)
                    if(travel[curr]==None):
                        curr=source
                    else:
                        curr=travel[curr]
                if(len(path)!=0):
                    print(source,end =" ")
                    for j in range(len(path)):
                        print(" - ", path[j],end=" ")
                    print(" - ",i)
                else:
                    print(source," - ", i)
            else:
                print(source)
