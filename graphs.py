from re import L


class Graph():
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            
            return False
        
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list.keys():
                if vertex in self.adj_list[v]:
                    self.adj_list[v].remove(vertex)
            
            del self.adj_list[vertex]
            return True
        
        return False

    def plot(self):
        for vertex in self.adj_list.keys():
            print(vertex, ": ", self.adj_list[vertex])
        
    
graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)

graph.add_edge(1,2)

graph.remove_edge(1,2)
graph.remove_vertex(2)
graph.plot()

