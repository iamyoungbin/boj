#include <stdio.h>

#define TREE_MAX_SIZE	10001

typedef struct Node{
	int col;
	int left;
	int right;
}Node;

typedef struct Queue{
	int column;
	int node;
}Queue;

Node bt[TREE_MAX_SIZE];
int rootCheck[TREE_MAX_SIZE] = {0, };

Queue q[TREE_MAX_SIZE];
int front = -1;
int rear = -1;

int idx = 1;
int objLvl = 1;
int maxWd = 1;

void dfs(int nodeNum)
{
	if(nodeNum == -1)	return;
	
	dfs(bt[nodeNum].left);
	bt[nodeNum].col = idx++;
	dfs(bt[nodeNum].right);
}

void levelOrder(int nodeNum)
{	
	q[++rear].node = nodeNum;
	q[rear].column = bt[nodeNum].col;
	
	int curLevel = 2;	
	while(front != rear){
		int end = rear;
		
		while(front != end){
			if(bt[q[front+1].node].left != -1){
				q[++rear].node = bt[q[front+1].node].left;
				q[rear].column = bt[q[rear].node].col;
			}
			
			if(bt[q[front+1].node].right != -1){
				q[++rear].node = bt[q[front+1].node].right;
				q[rear].column = bt[q[rear].node].col;
			}
				
			front++;
		}
		
		if(front != rear &&maxWd < q[rear].column - q[front+1].column + 1){
			objLvl = curLevel;
			maxWd = q[rear].column - q[front+1].column + 1;
		}
		
		curLevel++;
	}

}

int main(void)
{
	int N;
	scanf("%d", &N);
	getchar();
	
	int i;
	for(i = 0; i < N; i++){
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		getchar();
		
		if(rootCheck[a] != -1)	rootCheck[a] = 1;
		bt[a].left = b;
		bt[a].right = c;
		
		if(b != -1)		rootCheck[b] = -1;
		if(c != -1)		rootCheck[c] = -1;
	}
	
	int rootNum;
	for(i = 0;	; i++){
		if(rootCheck[i] == 1){
			rootNum = i;
			break;
		}
	}
	
	dfs(rootNum);
	levelOrder(rootNum);
	
	printf("%d %d\n", objLvl, maxWd);
	
	return 0;
}
