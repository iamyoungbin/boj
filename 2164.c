#include <stdio.h>

#define QMS	500001	// queue max size

int cq[QMS];
int front = 0;
int rear = 0;

void enqueue(int n){
	if(rear == QMS-1)	rear = 0;
	else				rear++;
	
	cq[rear] = n;
}

void dequeue(){
	if(front == QMS-1)	front = 0;
	else				front++;
}

void reverse(){
	dequeue();
	enqueue(cq[front]);
}

int main(void){
	int n;
	scanf("%d", &n);
	
	int i;
	for(i = 1; i <= n; i++)	enqueue(i);
	
	while((front % (QMS-1)) + 1 != rear){
		dequeue();
		reverse();
	}
	
	printf("%d", cq[rear]);
	
	return 0;
}
