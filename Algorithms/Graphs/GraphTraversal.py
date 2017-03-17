'''
    Undirected Graph Traversal:
        Breadth-First Search and
            Depth-First Search Implementations
    ===========================================
     INPUT:                         OUTPUT:
        Graph:                          BFS = [A, B, F]
                                        DFS = [A, B, C, D, F]
         START = A -- C -- E
                 |  / |
                 | /  |
                 B -- D
                 |  / |
                 | /  |
           END = F    G -- H
                           |
                           |
                           I

    Assuming this Data Structure:
    =============================
    class Graph(object):
        def __init__(self, graph=None):
            self.graph = graph

        def vertices(self):
            return list(self.graph.keys())

        def edges(self):
            return self.__generate_edges()

        def add_vertex(self, vertex):
            if vertex not in self.graph:
                self.graph[vertex] = []

        def add_edge(self, vertex1, vertex2):
            if vertex1 in self.graph:
                self.graph[vertex1].append(vertex2)
            else:
                self.graph[vertex1] = [vertex2]

        def __generate_edges(self):
            edges = []
            for vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if {neighbor, vertex} not in edges:
                        edges.append({neighbor, vertex})
            return edges
'''


def bfs(graph, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        u = path[-1]

        if u == end:
            return path

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                curr_path = path + [v]
                queue.append(curr_path)
    return None


def dfs(graph, node, end, visited=set(), path=[]):
    
    path = path + [node]

    if node == end:
        return path

    visited.add(node)

    for n in graph[node]:
        if n not in visited:
            p = dfs(graph, n, end, visited, path)
            if p:
                return p
    return None


if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
    		 'B': ['A', 'C', 'D', 'F'],
    		 'C': ['A', 'B', 'D', 'E'],
    		 'D': ['B', 'C', 'F', 'G'],
    		 'E': ['C'],
    		 'F': ['B', 'D'],
    		 'G': ['D', 'H'],
             'H': ['G', 'I'],
             'I': ['H']}

    print ("Breadth-First Search: %s " % bfs(graph, 'A', 'F'))
    print ("Depth-First Search: %s " % dfs(graph, 'A', 'F'))