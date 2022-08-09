#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES	100001

typedef struct Node{
	int vertex;
	int distance;
	struct Node *link;
}Node;

Node g[MAX_VERTICES];
int visited[MAX_VERTICES];

int max;
int end;

void initGraph(int num)
{
	int i;
	for(i = 1; i <= num; i++){
		g[i].link = NULL;
	}
}

void insertNode(int num, int nv, int nd)
{
	Node* newNode;
	newNode = (Node*)malloc(sizeof(Node));
	newNode->vertex = nv;
	newNode->distance = nd;
	
	newNode->link = g[num].link;
	g[num].link = newNode;
}

void deleteNode(int num)
{
	Node* delNode;
	Node* temp;
	delNode = g[num].link;
	
	while(delNode != NULL){
		temp = delNode->link;
		free(delNode);
		delNode = temp;
	}
	
	g[num].link = NULL;
}

void initVisited(int num)
{
	int i;
	for(i = 1; i <= num; i++)
		visited[i] = 0;
}

void dfs(int num, int dist)
{	
	Node* trailer = g[num].link;
	
	visited[num] = 1;
	
	if(dist > max){
			max = dist;
			end = num;
	}	
		
	while(trailer != NULL){
		if(!visited[trailer->vertex]){
			dfs(trailer->vertex, dist + trailer->distance);
		}
		trailer = trailer->link;
	}
}

int main(void)
{
	int v;
	scanf("%d", &v);
	
	initGraph(v);
	
	int i;
	for(i = 0; i < v; i++){
		int vnum, nv, nd;
		scanf("%d", &vnum);
		while(1){
			scanf("%d", &nv);
			if(nv == -1)	break;
			else{
				scanf("%d", &nd);
				insertNode(vnum, nv, nd);
			}
		}
	}
	
	initVisited(v);
	max = -1;
	dfs(1, 0);
	
	initVisited(v);
	max = -1;
	dfs(end, 0);
	
	printf("%d\n", max);
	
	for(i = 1; i <= v; i++){
		deleteNode(i);
	}
	
	return 0;
}
