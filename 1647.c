#include <stdio.h>

#define MAX_N_SIZE  100000
#define MAX_M_SIZE  1000000

typedef struct Edge{
    int vertex1;
    int vertex2;
    int weight;
}Edge;

Edge heap[MAX_M_SIZE+1];
int heapSize = 0;
int parent[MAX_N_SIZE+1];
int rank[MAX_N_SIZE+1];

void insertHeap(Edge e)
{
    int i = ++heapSize;

    while((i > 1) && (e.weight < heap[i/2].weight)){
        heap[i] = heap[i/2];
        i /= 2;
    }

    heap[i] = e;
}

Edge deleteHeap()
{
    int parent = 1, child = 2;
    Edge temp = heap[heapSize--], obj = heap[1];

    while(child <= heapSize){
        if((child < heapSize) && heap[child].weight > heap[child+1].weight)
            child++;
        if(temp.weight <= heap[child].weight)   break;

        heap[parent] = heap[child];
        parent = child;
        child *= 2;
    }
    heap[parent] = temp;

    return obj;
}

int find(int x)
{
    if(x == parent[x])  return x;

    return parent[x] = find(parent[x]);
}

void unionByRank(int x, int y)
{
    x = find(x);
    y = find(y);

    if(x != y){
        if(rank[x] > rank[y])   parent[y] = x;
        else                    parent[x] = y;

        if(rank[x] == rank[y])  rank[y]++;
    }
}

int kruskal(int n)
{
    int acceptedEdge = 0;
    int sum = 0;

    while(acceptedEdge < n-2){
        Edge temp = deleteHeap();

        if(find(temp.vertex1) != find(temp.vertex2)){
            unionByRank(temp.vertex1, temp.vertex2);
            sum += temp.weight;
            acceptedEdge++;
        }
    }

    return sum;
}

int main()
{
    int N, M;
    scanf("%d %d", &N, &M);

    int i;
    for(i = 1; i <= N; i++){
        parent[i] = i;
        rank[i] = 1;
    }
    for(i = 1; i <= M; i++){
        Edge temp;
        scanf("%d %d %d", &temp.vertex1, &temp.vertex2, &temp.weight);
        insertHeap(temp);
    }

    printf("%d\n", kruskal(N));

    return 0;
}

/*
    test case :

    6 8
    1 2 1
    1 3 3
    2 3 2
    1 4 2
    2 4 5
    3 4 4
    4 6 99
    5 6 90

    ans : 95

*/