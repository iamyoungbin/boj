#include <stdio.h>
#include <stdlib.h>

#define SHEEP	1
#define WOLF	2

typedef struct Node{
	int vertex;
	int obj;
	int num;
	struct Node *link;
}Node;

Node graph[123457];
int visited[123457] = {0, };
int N;

long long sum = 0;

void insertEdge(int v, int t, int n, int pv)
{
	Node *newNode;
	newNode = (Node*)malloc(sizeof(Node));
	
	newNode->vertex = v;
	newNode->obj = t;	
	if(t == WOLF)	n *= -1;
	newNode->num = n;
	graph[v].num = n;
	
	newNode->link = graph[pv].link;
	graph[pv].link = newNode;
}

long long dfs(int v)
{
	visited[v] = 1;
	long long sum = graph[v].num;
	
	Node* temp = graph[v].link;
	if(temp == NULL){
		if(sum > 0)	return sum;
		else		return 0;
	}
	
	for(temp = graph[v].link; temp; temp = temp->link){
		if(!visited[temp->vertex]){
			sum+= dfs(temp->vertex);
		}
	}
	
	if(sum > 0)	return sum;
	else		return 0;
}

int main(void)
{
	scanf("%d", &N);
	getchar();
	
	int i;
	for(i = 1; i <= N; i++){
		graph[i].link = NULL;
	}
	graph[1].num = 0;
	
	for(i = 2; i <= N; i++){
		char t;
		int a, p;
		scanf("%c %d %d", &t, &a, &p);
		getchar();
		
		if(t == 'S')	insertEdge(i, SHEEP, a, p);
		else			insertEdge(i, WOLF, a, p);	
	}
	
	//dfs(1, 0);
	printf("%lld\n", dfs(1));
	
	return 0;
}
