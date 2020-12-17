'''
	Given a starting vertex s, 
	traverse through the graph in adjancency matrix format in 
	depth-first manner.
'''
def stack_DFS(adj_mat, s):
	num_ver = len(adj_mat) #number of vertices
	explore_stack = [s] 
	explored = [False] * num_ver
	explored[s-1] = True
	while len(explore_stack) > 0:
		v = explore_stack.pop()
		if not explored[v-1]:
			explored[v-1] = True
			edges = adj_mat[v-1]
			for i in range(num_ver):
				if edges[i] == 1:
					explore_stack.append(i+1)

def stack_al_DFS(vertices, edges, s):
	num_ver = len(vertices)
	explore_stack = [s]
	explored = [False] * num_ver
	explored[s-1] = True
	while len(explore_stack) > 0:
		v = explore_stack.pop()
		if not explored[v-1]:
			explored[v-1] = True
			v_edges = edges[vertices[v-1]:vertices[v]]
			for vertex in v_edges:
				explore_stack.append(vertex)

def topo_sort(vertices, edges):
	num_ver = len(vertices)
	global curlabel = num_ver
	global explored = [False] * num_ver
	global labels = [0] * num_ver
	for v in range(num_ver):
		if not explored[v-1]: 
			DFS_Topo(vertices,edges, e)

def DFS_Topo(vertices, edges, v):
	v_edges = edges[vertices[v-1]:vertices[v]]
	explored[v-1] = True
	for vertex in v_edges:
		if not explored[vertex-1]:
			DFS_Topo(vertices, edges, vertex)
	labels[v-1] = curlabel
	curlabel -= 1
