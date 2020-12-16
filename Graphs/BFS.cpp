#include <vector>
#include <limits>
#include <queue>

// adjacency matrix version
void BFS(std::vector<std::vector<int>> graph, int s){
	int num_ver = graph.size();
	std::vector<bool> explored_vector (num_ver, false);
	std::vector<int> length_vector (num_ver, std::numeric_limits<int>::max());
	explored_vector[s-1] = true;
	length_vector[s-1] = 0;
	std::queue<int> q;
	q.push(s);
	while(!q.empty()){
		int v = q.front();
		q.pop();
		for (int i = 0; i < num_ver; i++){
			if (graph[v-1][i] == 1){
				if (explored_vector[i] == false){
					explored_vector[i] = true;
					length_vector[i] = length_vector[v-1] + 1;
					q.push(i+1);
				}	
			}
		}
	}
	return ;
}

//adjacency list version
void al_BFS(std::vector<int> vertices, std::vector<int> edges, int s){
	int num_vertices = vertices.size(); 
	std::vector<bool> explored(num_vertices, false); // list that represents whether a vertex i at index i-1 has been explored
	explored[s-1] = true; // starting vertex is explored
	std::queue<int> q;
	q.push(vertices[s-1]);
	while (!q.empty()){
		int v = q.front();
		q.pop();
		for (int i = vertices[v]; i < vertices[v+1]; i++){ //for all edges from v
			if (!explored[edges[i]]){ // if not explored, explore then add to queue
				explored[edges[i]] = true;
				q.push(edges[i]);
			}
		}
	}
	return ;
}

std::vector<int> UCC(std::vector<std::vector<int>> graph){
	int num_ver = graph.size();
	int num_cc = 0;
	std::vector<int> cc_vector(num_ver,0);
	for (int i = 0; i < num_ver; i++){
		if (cc_vector[i] == 0){
			num_cc++;
			cc_vector[i] = num_cc;
			std::queue<int> q;
			q.push(i+1);
			while(!q.empty()){
				int v = q.front();
				q.pop();
				for (int j = 0; j < num_ver; j++){
					if (graph[v-1][j] == 1){
						q.push(j+1);
						cc_vector[j] = num_cc;
					}
				}
			}
		}
	}
	return cc_vector;
}

std::vector<int> al_UCC(std::vector<int> vertices, std::vector<int> edges, int s){
	int num_ver = vertices.size();
	int num_cc = 0;
	std::vector<int> cc_vector(num_ver,0);
	for (int i = 0; i < num_ver; i++){
		if (cc_vector[i] == 0){
			num_cc++;
			cc_vector[i] = num_cc;
			std::queue<int> q;
			q.push(i+1);
			while(!q.empty()){
				int v = q.front();
				q.pop();
				for (int j = vertices[v]; j < vertices[v+1]; j++){
					int voi = edges[j];
					if(cc_vector[voi] == 0){				
						q.push(voi);
						cc_vector[voi] = num_cc;
					}
				}
			}
		}
	}
	return cc_vector;
}

