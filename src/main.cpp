#include "stdio.h"

#include "lib/lib_io.h"
#include "lib/lib_time.h"
#include "route.h"
int main(int argc, char *argv[]) {

	print_time("Begin");
	char *topo[MAX_EDGE_NUM];
	int edge_num;

	char *demand[MAX_DEMAND_NUM];
	int demand_num;
	char *srlg[MAX_SRLG_NUM];
	int srlg_num;

	char *topo_file = argv[1];
	edge_num = read_file(topo, MAX_EDGE_NUM, topo_file);
	if (edge_num == 0) {
		printf("Please input valid topo file.\n");
		return -1;
	}
	char *demand_file = argv[2];
	demand_num = read_file(demand, MAX_DEMAND_NUM, demand_file);
	if (demand_num != MAX_DEMAND_NUM) {
		printf("Please input valid demand file.\n");
		return -1;
	}

	char *srlg_file = argv[3];
	srlg_num = read_file(srlg, MAX_SRLG_NUM, srlg_file);
	if (srlg_num == 0) {
		printf("Please input valid srlg file.\n");
		return -1;
	}

	search_route(topo, edge_num, demand, demand_num, srlg, srlg_num);

	char *result_file = argv[4];
	write_result(result_file);
	release_buff(topo, edge_num);
	release_buff(demand, demand_num);
	release_buff(srlg, srlg_num);

	print_time("End");

	return 0;
}

