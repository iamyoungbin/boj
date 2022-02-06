#include <stdio.h>

typedef struct queue{
	int item;
	int ts;	// timestamp
}queue;

queue q[1000];
int rear = -1;
int front = -1;
int cnt = 1;
int tw = 0;	// total weight, <= 1000

void dequeue(){
	if(rear > front){
		tw -= q[++front].item;			
	}
}

void enqueue(int cw){
	q[++rear].item = cw;
	q[rear].ts = cnt++;
	
	tw += cw;
}

int main(void){
	int n, w, l;
	scanf("%d %d %d", &n, &w, &l);
	
	int i, cw;	// current weight
	for(i = 0; i < n; i++){
		scanf("%d", &cw);
		if(rear == front)	enqueue(cw);	// queue empty 
		else{
			while(cnt - q[front+1].ts >= w){	// dequeue 되어야 할 시간이 된 원소들을 dequeue, 현재시간 - q[front] 원소의 enqueue된 시간 >= 다리를 건너는 데 필요한 시간 
				if(rear == front)	break;
				dequeue();
			}
			
			while(tw + cw > l){		// 새로운 트럭이 enqueue 되었을 때, 토탈 중량 + 원소 충량이 다리 최대하중을 넘어가면, q[front] 원소가 dequeue 될 시간으로 이동 후, dequeue.  
				cnt = q[front+1].ts + w;
				dequeue();
			}	
			
			enqueue(cw);
		}
	}	
	
	printf("%d", cnt+w-1);	// enqueue 시에 기본적으로 cnt++ 연산을 하기 때문에 큐의 마지막 원소가 dequeue 될 때의 cnt는 -1을 해주어야 한다. 
	
	return 0;
}
