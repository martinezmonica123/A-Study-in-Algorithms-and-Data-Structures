############################################################
############################################################
######            Undirected Graph                    ######
#############################################################
#############################################################


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