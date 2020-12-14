import sys
import queue
'''
	Given G(V,E) in adjancency matrix, and a vertex s, with all edges length == 1, 
	return shortest length from s to some vertex v for all vertex v in V.
'''
def BFS(adj_mat, s):
	num_vertex = len(adj_mat) # number of vertices 
	explored_list = [False]*num_vertex # boolean list of whether the ith vertex has been explored
	length_list = [sys.maxsize]*num_vertex # length list of distance from s to the ith vertex
	explored_list[s-1] = True # initialize so that s is explored
	length_list[s-1] = 0 # initialize so that s is 0 away from itself
	q = queue.SimpleQueue() # initialize queue
	q.put(s) # and put s
	while not q.empty(): # while there exists a vertex to travel to
		v = q.get() # pop a vertex
		edges = adj_mat[v-1] # get the according row of adjancency matrix 
		for c in range(num_vertex): 
			if c != 0: # find the edge
				if explored_list[c] == False: #if not explored
					explored_list[c] = True # now explored
					length_list[c] = length_list[v-1] + 1 # assign length
					q.put(c+1) # put it in the queue!
	return length_list

'''
	Given G(V,E) in adjancency matrix, and a vertex s, with all edges length == 1, 
	return to which connected component a vertex v belongs to for all v in V.
'''
def UCC(adj_mat):
	num_vertices = len(adj_mat)
	cc_list = [0] * num_vertices
	num_CC = 0
	for i in range(num_vertices): # all vertices
		if cc_list[i] == 0: # if not explored
			num_CC += 1
			cc_list[i] = num_CC
			q = queue.SimpleQueue() # initialize queue
			q.put(s) # and put s
			while not q.empty(): # while there exists a vertex to travel to
				v = q.get() # pop a vertex
				edges = adj_mat[v-1] # get the according row of adjancency matrix 
				for c in range(num_vertices): 
					if c != 0: # find the edge
						if cc_list[c] == 0: #if not explored
							cc_list[c] = num_CC # now explored
							q.put(c+1) # put it in the queue!
	return cc_list










	