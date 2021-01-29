from Graph import *

graph = Graph()
for i in range(5):
    graph.add_vertex()
graph.add_edge(1,2,3)
graph.add_edge(1,4,4)
graph.add_edge(3,1,3)
graph.add_edge(3,0,3)
graph.add_edge(3,4,4)
graph.add_edge(2,0,1)
graph.add_edge(4,2,3)
graph.add_edge(0,1,6)
graph.print_graph()
graph.print_edges()
graph.dijkstra(2)
