/*
 * NetworkFlow.h
 *
 *  Created on: Jul 13, 2016
 *      Author: Taoheng
 */

#ifndef NETWORKFLOW_H_
#define NETWORKFLOW_H_

#include <vector>
#include"head.h"
using namespace std;
/*
 *
 */
class newtworkEdge {
public:
	int to, cap, rev, id;
	newtworkEdge(int t, int c, int r, int i) :
			to(t), cap(c), rev(r), id(i) {
	}
};
class newtworkEdgelist {
public:
	vector<newtworkEdge> newtworkedgelist;
};

class NetworkFlow {
public:
	int source, destination;
	vector<newtworkEdgelist> G;
	vector<int> used;
	int nodeSize;

	//dinic
	vector<int> level;

	NetworkFlow(Graph &graph, Request&request) {
		int from, to, cap, id;
		G = vector<newtworkEdgelist>(graph.nodeNum);
		nodeSize = graph.nodeNum;
		source = graph.source;
		destination = graph.destination;
		for (unsigned int i = 0; i < graph.edges.size(); i++) {
			from = graph.edges[i].from;
			to = graph.edges[i].to;
			id = graph.edges[i].id;
			cap = request.edgeCapacity.at(id); //graph.edges[i].capacity;

			cout << id << " " << graph.node_index[from] << " - "
					<< graph.node_index[to] << " - " << cap << endl;

			newtworkEdge e1(to, cap, G[to].newtworkedgelist.size(), id);
			G[from].newtworkedgelist.push_back(e1);
			newtworkEdge e2(from, cap, G[from].newtworkedgelist.size() - 1, id);
			G[to].newtworkedgelist.push_back(e2);
		}

	}
	void clearUsedVector() {
		used = vector<int>(nodeSize, false);
	}

};

extern void MaxFlowAlgorithm_fordfulkerson(Graph &graph, Request & request);

#endif /* NETWORKFLOW_H_ */
