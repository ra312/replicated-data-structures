from collections import defaultdict

from LWW.Set import Set
class Graph:
    def __init__(self):
        # self.graph = defaultdict(list)
        self.vertices = Set()
        self.edges = defaultdict(Set)
    def addVertex(self, vertex):
        self.vertices.add(vertex)
    def removeVertex(self, vertex):
        self.vertices.remove(vertex)
    def exists(self, vertex):
        '''
        check if a vertex exists in the graph
        '''
        return self.vertices.exists(vertex)
    def addEdge(self, vertex_A, vertex_B):
        
        self.edges[vertex_A].add(vertex_B)
        
        #if vertex_A is connected with vertex_B iff
        # there exists vertex_B in self.graph[vertex_A]

    def removeEdge(self, vertex_A, vertex_B):
        # vertex_B is unique and we remove vertex_B
        self.edges[vertex_A].remove(vertex_B)
        # now we remove vertex_A
        del self.edges[vertex_A]
    def adjacentVertices(self, vertex):
        '''
        return all vertices connected with the given vertex
        return -1 if there are no vertices connected
        '''
        if self.vertices.exists(vertex):
            if vertex in self.edges:
                return self.edges[vertex]
        return -1
    def isTherePath(self, vertex_A, vertex_B):
        '''
        I chose to use classical breadth-first search (BFS) algorithm
        '''
        visited = [False]*self.vertices
        queue = []
        queue.append(vertex_A)
        
        while queue:
            n = dequeu.pop(0)
            if n == vertex_B:
                return True
            for vertex in self.edges[vertex_A]:
                # how we loop over our custom Set class?
                if visited[vertex]==False:
                    queue.append(vertex)
                    visited[vertex]=True
        # If BFS is complete without vertex_B visited
        return False

    def merge(self, other):
        self.vertices.merge(other.vertices)
        self_vertices = self.edges.keys()
        for vertex in self.edges.keys():
            if vertex in other.edges:
                self.edges[vertex].merge(other.edges[vertex])
        # self.edges.merge(other.edges)


        
    