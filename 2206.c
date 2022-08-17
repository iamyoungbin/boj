#include <stdio.h>

#define MAP_SIZE	1000
#define QUEUE_SIZE	1000000

typedef struct Node{
	int qn;
	int qm;
	int qwc;
}Node;

int map[MAP_SIZE][MAP_SIZE];
int visited[MAP_SIZE][MAP_SIZE][2] = {0, };

int N, M;
int dn[4] = {1, -1, 0, 0};
int dm[4] = {0, 0, -1, 1};

Node queue[QUEUE_SIZE];
int front = 0;
int rear = 0;

void enqueue(int pn, int pm, int pwc)
{
	Node temp = {pn, pm, pwc};
	rear = ++rear % QUEUE_SIZE;
	
	queue[rear] = temp;
}

Node dequeue()
{
	front = ++front % QUEUE_SIZE;
	return queue[front];
}

int bfs()
{	
	enqueue(0, 0, 0);
	visited[0][0][0] = visited[0][0][1] = 1;
	
	while(!(front == rear)){
		Node temp = dequeue();
		if(temp.qn == N-1 && temp.qm == M-1)	return visited[N-1][M-1][temp.qwc];
		
		int i;
		for(i = 0; i < 4; i++){
			int nn = temp.qn + dn[i];
			int nm = temp.qm + dm[i];
			
			if(nn >= 0 && nn < N && nm >= 0 && nm < M){
				if(map[nn][nm] == 0 && !visited[nn][nm][temp.qwc]){
					enqueue(nn, nm, temp.qwc);
					visited[nn][nm][temp.qwc] = visited[temp.qn][temp.qm][temp.qwc] + 1;
				}
				else if(map[nn][nm] == 1){
					if(temp.qwc == 0 && !visited[nn][nm][1]){
						enqueue(nn, nm, 1);
						visited[nn][nm][1] = visited[temp.qn][temp.qm][temp.qwc] + 1;
					}
				}
			}
		}
	}

	return -1;
}

int main(void)
{
	scanf("%d %d", &N, &M);
	
	int i, j;
	for(i = 0; i < N; i++){
		for(j = 0; j < M; j++){
			int temp;
			scanf("%1d", &temp);
			map[i][j] = temp;
		}
	}
	
	printf("%d\n", bfs());

	return 0;
}
