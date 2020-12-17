#include <vector>
#include <limits>
#include <stack>

void stack_al_DFS(std::vector<int> vertices, std::vector<int> edges, int s){
	int num_ver = vertices.size();
	std::stack<int> to_be_explored;
	std::vector<bool> explored;
	explored[s-1] = true;
	while(!to_be_explored.empty()){
		int v = to_be_explored.top();
		to_be_explored.pop();
		if(!explored[v-1]){
			explored[v-1] = true;
			std::vector<int> v_edges;
			copy(vertices[v-1],vertices[v],v_edges);
			for (int vertex : v_edges){
				to_be_explored.push(vertex);
			}
		}
	}
}

int curlabel;
std::vector<bool> explored;
std::vector<int> labels;

void dfs_topo(std::vector<int> vertices, std::vector<int> edges, int v){
	int num_ver = vertices.size();
	explored[v-1] = true;
	std::vector<int> v_edges;
	copy(edges[vertices[v-1]],edges[vertices[v]],v_edges);
	for (int vertex : v_edges){
		if (!explored[vertex-1]){
			dfs_topo(vertices, edges, v);
		}
	}
	labels[v-1] = curlabel;
	curlabel--;
}

std::vector<int> topo_sort(std::vector<int> vertices, std::vector<int> edges){
	int num_ver = vertices.size();
	explored = std::vector<bool> (num_ver, false);
	curlabel = num_ver;
	for (int v : vertices){
		if (!explored[v-1]){
			dfs_topo(vertices, edges, v);
		}
	}
	return labels;
}
