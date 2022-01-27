#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_SIZE 2000000

int queue[MAX_SIZE];
int rear = -1;
int front = -1;

bool isEmpty(){
	if(rear == front)	return true;
	else				return false;
}

void push(int x){
	queue[++rear] = x;
}

void pop(){
	if(isEmpty())	printf("-1\n");
	else			printf("%d\n", queue[++front]);
}

void size(){	
	printf("%d\n", rear-front);
}

void getFront(){
	if(isEmpty())	printf("-1\n");
	else			printf("%d\n", queue[front+1]);
}

void getBack(){
	if(isEmpty())	printf("-1\n");
	else			printf("%d\n", queue[rear]);
}

int main(void){
	int n, i, e;
	char cmd[6];	// 5 + '\0'
	
	scanf("%d", &n);
	
	for(i = 0; i < n; i++){
		scanf("%s", cmd);	// scanf until ~ ' '
		
		if(strcmp(cmd, "push") == 0){
			scanf("%d", &e);
			push(e);
			continue;
		}
		if(strcmp(cmd, "pop") == 0){
			pop();
			continue;
		}
		if(strcmp(cmd, "size") == 0){
			size();
			continue;
		}
		if(strcmp(cmd, "empty") == 0){
			if(isEmpty())	printf("1\n");
			else			printf("0\n");
			continue;
		}
		if(strcmp(cmd, "front") == 0){
			getFront();
			continue;
		}
		if(strcmp(cmd, "back") == 0){
			getBack();
			continue;
		}
	}
	return 0;
}
