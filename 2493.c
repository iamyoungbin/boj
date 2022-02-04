#include <stdio.h>

#define MAX_TW 100000000

typedef struct tower{
	int height;
	int idx;
}tower;

tower stack[500000];
int top = -1;

void push(int i, int h){
	top++;
	stack[top].idx = i;
	stack[top].height = h;
}

int peek(){
	if(top == -1)	return MAX_TW;
	
	return stack[top].height;
}

void pop(){
	top--;
}

int main(void){
	int n;
	
	scanf("%d", &n);
	
	int i, h;
	for(i = 1; i <= n; i++){
		scanf("%d", &h);
		
		if(top == -1){	// stack empty
			push(i, h);
			printf("0 ");
		}
		else{
			while(peek() < h)	pop();
			
			if(top == -1)	printf("0 ");	// stack empty
			else			printf("%d ", stack[top].idx);
			
			push(i, h);
		}		
	}	
	
	return 0;
}
