'''

	Minimum Spanning Tree:
		A subset of a connected (weighted and directed) graph that connects all 
		vertices together with out any cycles and with the minimum possible total weight.
		
		Prim's Algorithm:
			Build the MST one vertex at a time.

'''


def get_min(distance, vertices):
	''' Prims() Helper Function 
	
		Recursive Function:
		Returns the min element in a 'distance' dictionary such that 
		the resulting node is not in the 'vertices' set.

		Arguments:
			distance [dictionary] -- all paths from 'start' and their total cost
			vertices [set] -- all vertices in a graph
		
		Returns:
			Base Case:
				node_to -- node A in min cost edge 
				node_from -- node B in min cost edge
				min_cost [int] -- cost of going from 'node_to' to 'node_from'

			Recursive Case
				distance [dictionary] -- all paths from 'start' and their total cost
				vertices [set] -- all vertices in a graph
	'''
	node_to, node_from = min(distance.keys(), key=distance.get)
	min_cost = distance[(node_to, node_from)]
	
	if node_from in vertices:
		return (node_to, node_from, min_cost)
	else:
		del distance[(node_to, node_from)]
		return get_min(distance, vertices)


def prims(graph, start):
	''' Minimum Spanning Tree
	
	Prim's Algorithm
	Build the edge list one vertex at a time repeatedly select the smallest 
	weight edge that will enlarge the number of vertices in the graph.
	
	Arguments:
		graph [dictionary] -- dictionary of dictionaries 
							to detail edge and edge costs
		start -- starting node

	Returns:
		path [list] -- list of tuples of vertices representing paths taken
		cost [int] -- the total cost of the mst
	'''
	path, cost = [], 0
	distance = {(None, start): 0}
	vertices = set(graph.keys())

	while vertices:

		node_to, node_from, min_cost = get_min(distance, vertices)
		
		vertices.remove(node_from)
		del distance[(node_to, node_from)]

		for node in graph[node_from].keys():
			if node in vertices:
				node_cost = graph[node_from][node]
				distance[(node_from, node)] = node_cost
				
		path.append((node_to, node_from))
		cost += min_cost	
	return (path, cost)


graph = {'a': {'b': 10, 'c': 3},
		 'b': {'a': 10, 'c': 5, 'd': 7, 'e': 4},
		 'c': {'a': 3, 'b': 5, 'd': 3, 'e': 6},
		 'd': {'b': 7, 'c': 3, 'e': 2, 'f': 1},
		 'e': {'c': 6, 'b': 4, 'd': 2, 'f': 3},
		 'f': {'d': 1, 'e': 3}}

graph1 = {'a': {'b':5, 'c':3},
		  'b': {'a':5, 'c':2, 'd':1},
		  'c': {'a':5, 'b':2, 'd':4},
		  'd': {'b':2, 'c': 4} }

print( prims(graph, 'a'))
print( prims(graph1, 'a'))