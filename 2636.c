#include <stdio.h>

#define MAX_SIZE	100
#define QUE_SIZE	10001

#define CHEESE		1
#define MEL_CHEESE	2
#define INS_AIR		0
#define OUTS_AIR	-1

typedef struct Node{
	int y;
	int x;
}Point;

int map[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE] = {0, };
int dn[4] = {1, -1, 0, 0};
int dm[4] = {0, 0, -1 ,1};
int N, M;
int mc;

Point queue[QUE_SIZE];
int rear = 0;
int front = 0;

void enqueue(int n, int m)
{
	Point temp = {n, m};
	rear = ++rear % QUE_SIZE;
	queue[rear] = temp;
}

Point dequeue()
{
	front = ++front % QUE_SIZE;
	return queue[front];
}

int isEmpty()
{
	if(front == rear)	return 1;
	else				return 0;
}

void melt()
{
	int i, j;
	for(i = 0; i < N; i++){
		for(j = 0; j < M; j++){
			if(map[i][j] == 2){
				mc++;
				map[i][j] = 0;
			}	
		}
	}
}

int meltCheck()
{
	int i, j;
	for(i = 0; i < N; i++){
		for(j = 0; j < M; j++){
			if(map[i][j] == 1)	return 1;
		}
	}
	
	return 0;
}

void initVisited()
{
	int i, j;
	for(i = 0; i < N; i++){
		for(j = 0; j < M; j++){
			visited[i][j] = 0;
		}
	}
}

void bfs()
{
	enqueue(0, 0);
	visited[0][0] = 1;
	
	while(!isEmpty()){
		Point temp = dequeue();
		
		int i;
		for(i = 0; i < 4; i++){
			int nn = temp.y + dn[i];
			int nm = temp.x + dm[i];
			
			if(nn >= 0 && nn < N && nm >= 0 && nm < M){
				if(!visited[nn][nm]){
					if(map[nn][nm] == 1)	map[nn][nm] = 2;
					else if(map[nn][nm] == 0 || map[nn][nm] == -1){
						map[nn][nm] = -1;
						visited[nn][nm] = 1;
						enqueue(nn, nm);
					}
				}
			}
		}
	}
}

int main(void)
{
	scanf("%d %d", &N, &M);
	
	int i, j;
	for(i = 0; i < N; i++){
		for(j = 0; j < M; j++){
			scanf("%d", &map[i][j]);
			if(i == 0 || j == 0 || i == N-1 || j == M-1)	map[i][j] = OUTS_AIR;
		}
	}
	
	int time = 0;
	
	while(meltCheck()){
		mc = 0;
		initVisited();
		
		bfs();		
		melt();
		time++;
	}
	
	printf("%d\n", time);
	printf("%d\n", mc);
	
	return 0;
}
