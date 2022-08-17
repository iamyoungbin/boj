#include <stdio.h>
#include <stdlib.h>

#define MAX_NODE_SIZE	10001

typedef struct Node{
	int vertex;
	int weight;
	struct Node *link;
}Node;

typedef struct GraphType{
	int num;
	Node *list[MAX_NODE_SIZE];
}GraphType;

int visited[MAX_NODE_SIZE];
int max, end;

void initGraph(GraphType *g, int n)
{
	g->num = n;
	
	int i;
	for(i = 0; i < MAX_NODE_SIZE; i++)
		g->list[i] = NULL;
}

void insertEdge(GraphType *g, int n1, int n2, int w)
{
	Node *newNode;
	
	newNode = (Node*)malloc(sizeof(Node));
	newNode->vertex = n2;
	newNode->weight = w;
	
	newNode->link = g->list[n1];
	g->list[n1] = newNode;
}

void dfs(GraphType *g, int pn, int pw)
{
	Node *temp;
	visited[pn] = 1;
	
	if(pw > max){
		max = pw;
		end = pn;
	}
	
	for(temp = g->list[pn]; temp; temp = temp->link){
		if(!visited[temp->vertex])
			dfs(g, temp->vertex, pw + temp->weight);
	}
}

void initVisited()
{
	max = 0;	
	int i;
	for(i = 0; i < MAX_NODE_SIZE; i++)
		visited[i] = 0;
}

int main(void)
{
	int n;
	scanf("%d", &n);
	
	GraphType g;
	initGraph(&g, n);
	
	int i;
	for(i = 0; i < n-1; i++){
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		insertEdge(&g, a, b, c);
		insertEdge(&g, b, a, c);
	}
	
	initVisited();
	dfs(&g, 1, 0);
	
	initVisited();
	dfs(&g, end, 0);
	
	printf("%d\n", max);
	
	return 0;
}
