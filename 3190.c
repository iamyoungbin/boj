#include <stdio.h>

#define WALL	-1
#define BLANK	0
#define SNAKE	1
#define APPLE	2

typedef struct Command{
	char c;
	int ts;	// timestamp
}Command;

typedef struct Queue{
	int xp;	// XPoint
	int yp;	// YPoint
}Queue;

typedef struct Vector{
	int xv;
	int yv;
}Vector;

int board[102][102];

Command cmd[100];
int front = -1;
int rear = -1;

Queue cq[10001];	// circular queue
int head = 0;	// rear
int tail = 0;	// front

Vector vec[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int vp = 0;

void Enqueue(int x, int y)
{
	if(++head == 10002)	head = 0;
	cq[head].xp = x;
	cq[head].yp = y;
	board[y][x] = SNAKE;
}

void Dequeue()
{	
	if(++tail == 10002)	tail = 0;
	board[cq[tail].yp][cq[tail].xp] = BLANK;
}

int Move()
{
	int objx, objy;
	
	objx = cq[head].xp + vec[vp].xv;
	objy = cq[head].yp + vec[vp].yv;
	
	switch(board[objy][objx]){
		case -1 :	// fail(bcuz wall)
			return 0;
			break;
		case 0 :	// blank
			Enqueue(objx, objy);
			Dequeue();
			break;
		case 1 :	// fail(bcuz snake)
			return 0;
			break;
		case 2 :	// apple
			Enqueue(objx, objy);
			break;	
		default :
			break;
	}
	
	return 1;
}

int main(void){
	int n, k, l;
	scanf("%d", &n);
	int i, j;
	for(i = 0; i <=n+1; i++){	// board initiating
		for(j = 0; j <= n+1; j++){
			if(i == 0 || i == n+1 || j == 0 || j == n+1)	board[i][j] = WALL;
			else											board[i][j] = BLANK;
		}
	}
	board[i][j] = SNAKE;	// snake initiating

	scanf("%d", &k);
	for(i = 0; i < k; i++){	// apple coordinate
		int x, y;
		scanf("%d %d", &y, &x);
		board[y][x] = APPLE;
	}
	
	scanf("%d", &l);
	for(i = 0; i < l; i++){
		int t;
		char c;
		scanf("%d %c", &t, &c);
		cmd[++rear].c = c;
		cmd[rear].ts = t;
	}
	
	cq[++head].xp = 1;	// starting point
	cq[head].yp = 1;		
	
	int cnt = 1;
	while(1){
		if(!Move())	break;	
		
		if(cnt == cmd[front+1].ts){
			front++;
			switch(cmd[front].c){
				case 'L' :
					//printf("cnt = %d, cmd %c, %d // ", cnt,cmd[front].c, cmd[front].ts);
					if(--vp == -1)	vp = 3;
					break;
				case 'D' :
					//printf("cnt = %d, cmd %c, %d // ", cnt,cmd[front].c, cmd[front].ts);
					if(++vp == 4)	vp = 0;
					break;
				default :
					break;
			}
		}

		//printf("%d %d // %d %d\n", cq[head].xp, cq[head].yp, cq[tail+1].xp, cq[tail+1].yp);	
		cnt++;
	}
	
	printf("%d", cnt);
	
	return 0;
}
