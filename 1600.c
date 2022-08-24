#include <stdio.h>

#define MAX_SIZE	200
#define MAX_K_SIZE	30
#define QUE_SIZE	40001

typedef struct Node{
	int w;
	int h;
	int hc;	// horsecount
	int wc;	// walkcount
}Node;

int hdW[8] = {-2, -1, 1, 2, -2, -1, 1, 2};	// horse dw
int hdH[8] = {-1, -2, -2, -1, 1, 2, 2, 1};	// horse dh
int mdW[4] = {0, 0, -1, 1};	// monkey dw
int mdH[4] = {1, -1, 0, 0};	// monkey dh

int map[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE][MAX_K_SIZE+1] = {0, };
int W, H, K;

Node queue[QUE_SIZE];
int front = 0, rear = 0;

int cnt = -1;

void enqueue(int tx, int ty, int thc, int twc)
{
	Node temp = {tx, ty, thc, twc};
	rear = ++rear % QUE_SIZE;
	queue[rear] = temp;
}

Node dequeue()
{
	front = ++front % QUE_SIZE;
	return queue[front];
}

void bfs()
{
	enqueue(0, 0, 0, 0);
	visited[0][0][0] = 1;
	
	int obj = 0;
	
	while(front!=rear){
		int x, y, i;
		Node temp = dequeue();
		
		if(temp.w == W-1 && temp.h == H-1){
			cnt = temp.wc;
			return;
		}
		
		if(temp.hc < K){
			for(i = 0; i < 8; i++){
				x = temp.w + hdW[i];
				y = temp.h + hdH[i];
				
				if(x >= 0 && x < W && y >= 0 && y < H && map[y][x] == 0){
					if(!visited[y][x][temp.hc+1]){
						visited[y][x][temp.hc+1] = 1;
						enqueue(x, y, temp.hc+1, temp.wc+1);
					}
				}
			}
		}
		
		for(i = 0; i < 4; i++){
			x = temp.w + mdW[i];
			y = temp.h + mdH[i];
				
			if(x >= 0 && x < W && y >= 0 && y < H && map[y][x] == 0){
				if(!visited[y][x][temp.hc]){
					visited[y][x][temp.hc] = 1;
					enqueue(x, y, temp.hc, temp.wc+1);
				}
			}
		}
		
		
	}
}

int main()
{
	scanf("%d", &K);
	scanf("%d %d", &W, &H);
	
	int i, j;
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++)	scanf("%d", &map[i][j]);	
	}
	
	bfs();
	
	printf("%d\n", cnt);
}
