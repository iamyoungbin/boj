#include <stdio.h>
#include <stdbool.h>

int stack[100000];
int top = -1;

int peek(){
	if(top == -1)	return 0;
	
	return stack[top];
}

void pop(){
	top--;
}

void push(int n){
	stack[++top] = n;
}

int main(void){
	
	int i, n, cnt, emt, idx;	// count, element, index
	bool sol = true;
	char result[200000];
	
	scanf("%d", &n);
	
	idx = 0;
	cnt = 1;
	for(i = 0; i < n; i++){
		scanf("%d", &emt);
		
		while(peek() < emt){
			push(cnt++);
			result[idx++] = '+';
		}
		
		if(peek() == emt){
			pop();
			result[idx++] = '-';
		}
		else{
			sol = false;
			break;
		}	
	}
	
	if(sol){
		for(i = 0; i < idx; i++)	printf("%c\n", result[i]);
	}
	else	printf("NO");
	
	return 0;
}
