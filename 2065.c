#include <stdio.h>
#include <string.h>

#define	LEFT	1
#define	RIGHT	2

#define TIME_MAX	200000

int rst[10000];
typedef struct Queue{
	int ts;
	int seq;
}Queue;

Queue lq[10000];
int lfront = -1;
int lrear = -1;

Queue rq[10000];
int rfront = -1;
int rrear = -1;

int boat = LEFT;
int time = 0;

int Peek(int side)
{
	if(side == LEFT){
		if(lfront == lrear)	return TIME_MAX;
		else				return lq[lfront+1].ts;
	}
	else{	// side == RIGHT
		if(rfront == rrear)	return TIME_MAX;
		else				return rq[rfront+1].ts;
	}
}

void Dequeue(int at)
{
	if(boat == LEFT){
		if(lfront == lrear)	{
			printf("Error : lfront == lrear\n");
			return;
		}
		rst[lq[++lfront].seq] = time + at;
	}
	else{	// boat == RIGHT
		if(rfront == rrear)	{
			printf("Error : rfront == rrear\n");
			return;
		}	
		rst[rq[++rfront].seq] = time + at;
	}
}

int Compare()
{
	if(lfront == lrear && rfront == rrear)	return -1;
	if(lfront == lrear) return RIGHT;
	if(rfront == rrear) return LEFT;
	
	if(boat == LEFT)	return Peek(LEFT) <= Peek(RIGHT) ? LEFT : RIGHT;
	else				return Peek(LEFT) < Peek(RIGHT) ? LEFT : RIGHT;
	
}

void Adjustment(int l)
{
	if(boat == LEFT){
		switch(Compare()){
			case LEFT :
				time = lq[lfront+1].ts;
				break;
			case RIGHT :
				boat = RIGHT;
				time = time+l >= rq[rfront+1].ts + l ? time + l : rq[rfront+1].ts + l;
				break;
			default :
				break;				
		}
	}
	else{	// boat == RIGHT
		switch(Compare()){
			case RIGHT :
				time = rq[rfront+1].ts;
				break;
			case LEFT :
				boat = LEFT;
				time = time+l >= lq[lfront+1].ts + l ? time + l : lq[lfront+1].ts + l;
				break;
			default :
				break;				
		}
	}
}

int main(void)
{
	int M, l, N;
	scanf("%d %d %d", &M, &l, &N);
	
	int i, cnt = 0;
	for(i = 0; i < N; i++){
		int temp;
		char cmd[6];
		scanf("%d %s", &temp, cmd);
		
		if(strcmp(cmd, "left") == 0){
			lq[++lrear].ts = temp;
			lq[lrear].seq = cnt++;
		}
		else{
			rq[++rrear].ts = temp;
			rq[rrear].seq = cnt++;
		}
	}
	
	int window = 0;	
	while(1){
		if((lfront == lrear) && (rfront == rrear))	break;
		
		if(Peek(boat) <= time){
			while(Peek(boat) <= time && window < M){
				Dequeue(l);
				window++;
			}
			
			time += l;
			boat = boat==LEFT ? RIGHT : LEFT;
			//printf("Side : %d -> %d \t\t // ", boat==LEFT ? RIGHT : LEFT ,boat);
		}
		else{
			Adjustment(l);
			//printf("Adjust Side : %d \t // ", boat);
		}	
		//printf("Time : %d \t Window : %d\n", time, window);
		window = 0;
	}
	
	for(i = 0; i < N; i++){
		printf("%d\n", rst[i]);
	}
	
	return 0;
}
