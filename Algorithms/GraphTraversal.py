
############################################################
######            Undirected Graph Traversal          ######
############################################################


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
                temp_path = path + [v]
                queue.append(temp_path)
    return None


def dfs(graph, node, end, visited=set(), path=[]):
    # def _dfs(graph, node, end, visited, path):
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


graph = {'A': ['B', 'C'],
		 'B': ['A', 'C', 'D','F'],
		 'C': ['A','B','D','E'],
		 'D':['B','C','F','G'],
		 'E': ['C'],
		 'F':['B', 'D'],
		 'G':['D', 'H'],
         'H': ['G', 'I'],
         'I': ['H'] }

print "Breadth-First Search: %s " % bfs(graph2, 'A', 'F')
print "Depth-First Search: %s " % dfs(graph2, 'A', 'F')

#############################################################


#  INPUT:

#             Graph:
#
#      START = A -- C -- E
#              |  / |
#              | /  |
#              B -- D
#              |  / |
#              | /  |
#        END = F    G -- H
#                        |
#                        |
#                        I


# OUTPUT:

#   BFS = [A, B, F]
#   DFS = [A, B, C, D, F]
#
