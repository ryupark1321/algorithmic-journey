'''
	Given a starting vertex s, 
	traverse through the graph in adjancency matrix format in 
	depth-first manner.
'''
def stack_DFS(adj_mat, s):
	num_ver = len(adj_mat)
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






