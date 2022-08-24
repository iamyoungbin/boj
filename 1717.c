#include <stdio.h>

#define MAX_N_SIZE	1000001

int parent[MAX_N_SIZE];
int rank[MAX_N_SIZE];

int n, m;

void initSet()
{
	int i;
	for(i = 0; i <= n; i++){
		parent[i] = i;
		rank[i] = 1;
	}
}

int find(int v)
{
	if(v == parent[v])	return v;
	else				return parent[v] = find(parent[v]);
}

void unionByRank(int v1, int v2)
{
	int pv1 = find(v1);
	int pv2 = find(v2);
	if(pv1 != pv2){
		if(rank[pv1] > rank[pv2])	parent[pv2] = pv1;
		else						parent[pv1] = pv2;
		
		if(rank[pv1] == rank[pv2])	rank[pv2]++;
	}
}

int main()
{
	scanf("%d %d", &n, &m);
	
	initSet();
	
	int i;
	for(i = 0; i < m; i++){
		int c, a, b;
		scanf("%d %d %d", &c, &a, &b);
		
		if(c == 0)	unionByRank(a, b);
		else{
			if(find(a) == find(b))	printf("YES\n");
			else					printf("NO\n");
		}
	}
	
	return 0;
}
