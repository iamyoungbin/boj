#include <stdio.h>

#define MAX_V_SIZE	10001
#define MAX_E_SIZE	100001

typedef struct Edge{
	int vertex1;
	int vertex2;
	int weight;
}Edge;

Edge heap[MAX_E_SIZE];
int heapSize = 0;

int parent[MAX_V_SIZE];
int rank[MAX_V_SIZE];

int V, E;
int edgeAccepted = 0;
int fullWeight = 0;

void insertHeap(Edge e)
{
	int i = ++heapSize;
	
	while((i>1) && e.weight < heap[i/2].weight){
		heap[i] = heap[i/2];
		i /= 2;
	}

	heap[i] = e;
}

Edge deleteHeap()
{
	int pt = 1, cd = 2;
	Edge item, temp;
	
	item = heap[1];
	temp = heap[heapSize--];
	
	while(cd <= heapSize){
		if((cd < heapSize) && heap[cd].weight > heap[cd+1].weight)	
			cd++;
		if(temp.weight <= heap[cd].weight)	break;
		
		heap[pt] = heap[cd];
		pt = cd;
		cd *= 2;
	}
	
	heap[pt] = temp;
	return item;
}

int find(int x)
{
	if(x == parent[x])	return x;
	else				return parent[x] = find(parent[x]);
}

void unionByRank(int x, int y)
{
	int px = find(x);
	int py = find(y);
	
	if(x != y){
		if(rank[x] < rank[y])	parent[x] = y;
		else					parent[y] = x;
		
		if(rank[x] == rank[y])	rank[x]++;
	}
}

void kruskal()
{
	while(edgeAccepted < V-1){
		Edge temp = deleteHeap();
		
		int uset = find(temp.vertex1);
		int vset = find(temp.vertex2);
		
		if(uset != vset){
			edgeAccepted++;
			//printf("Choose %dnd / %d-%d, weight = %d/ %d + %d\n", edgeAccepted, temp.vertex1, temp.vertex2, fullWeight+temp.weight, fullWeight, temp.weight);
			fullWeight += temp.weight;
			unionByRank(uset, vset);
		}
	}
}

int main(void)
{
	scanf("%d %d", &V, &E);
	int i;
	for(i = 1; i <= E; i++){
		Edge e;
		scanf("%d %d %d", &e.vertex1, &e.vertex2, &e.weight);
		insertHeap(e);
		if(i <= V){
			parent[i] = i;
			rank[i] = 1;
		}
	}

	kruskal();
	
	printf("%d\n", fullWeight);
	return 0;
}
