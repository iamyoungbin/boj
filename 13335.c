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
			while(cnt - q[front+1].ts >= w){	// dequeue �Ǿ�� �� �ð��� �� ���ҵ��� dequeue, ����ð� - q[front] ������ enqueue�� �ð� >= �ٸ��� �ǳʴ� �� �ʿ��� �ð� 
				if(rear == front)	break;
				dequeue();
			}
			
			while(tw + cw > l){		// ���ο� Ʈ���� enqueue �Ǿ��� ��, ��Ż �߷� + ���� �淮�� �ٸ� �ִ������� �Ѿ��, q[front] ���Ұ� dequeue �� �ð����� �̵� ��, dequeue.  
				cnt = q[front+1].ts + w;
				dequeue();
			}	
			
			enqueue(cw);
		}
	}	
	
	printf("%d", cnt+w-1);	// enqueue �ÿ� �⺻������ cnt++ ������ �ϱ� ������ ť�� ������ ���Ұ� dequeue �� ���� cnt�� -1�� ���־�� �Ѵ�. 
	
	return 0;
}
