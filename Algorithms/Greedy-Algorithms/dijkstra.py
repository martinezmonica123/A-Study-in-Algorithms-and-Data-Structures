'''
	Shortest Path: Single Sourced
		Dijkstra's Algorithm

'''

def dijkstra(graph, start):
	'''[summary]
	
	[description]
	
	Arguments:
		graph [dictionary] -- dictionary of dictionaries 
							to detail edge and edge costs
		start [string] -- starting node
	
	Returns:
		distance [dictionary] -- all paths from 'start' and their total cost
		previous [dictionary] -- path nodes and their parent nodes 
								(for path reconstruction)
	'''
	distance = {start: 0}
	previous = {}
	nodes = set(graph.keys())
	visited = set()

	while nodes:
		unvisited = list(set(distance.keys()) - visited)
		#print (unvisited)
		min_elem = min(unvisited, key=distance.get)
		min_weight = distance[min_elem]

		nodes.remove(min_elem)

		for edge in graph[min_elem].keys():
			weight = min_weight + graph[min_elem][edge]
			if edge not in distance or weight < distance[edge]:
				distance[edge] = weight
				previous[edge] = min_elem
		visited.add(min_elem)
	return (distance, previous)


graph1 = {'a': {'b':5, 'c':3},
		  'b': {'a':5, 'c':2, 'd':1},
		  'c': {'a':5, 'b':2, 'd':4},
		  'd': {'b':2, 'c': 4} }

graph = {'a': {'b': 10, 'c': 3},
		 'b': {'a': 10, 'c': 5, 'd': 7, 'e': 4},
		 'c': {'a': 3, 'b': 5, 'd': 3, 'e': 6},
		 'd': {'b': 7, 'c': 3, 'e': 2, 'f': 1},
		 'e': {'c': 6, 'b': 4, 'd': 2, 'f': 3},
		 'f': {'d': 1, 'e': 3}}

print(dijkstra(graph, 'a'))
