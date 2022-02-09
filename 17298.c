#include <stdio.h>

#define MS	1000000

int qst[MS];
int rst[MS];

int stack[MS];
int top = -1;

int main(void){
	int n;
	scanf("%d", &n);
	
	int i, temp;
	for(i = 0; i < n; i++){
		scanf("%d", &temp);
		qst[i] = temp;
	}
	
	rst[n-1] = -1;
	stack[++top] = qst[n-1];
	for(i = n-2; i >=0; i--){
		while(stack[top] <= qst[i]){
			if(--top == -1)	break;
		}
		if(top == -1)	rst[i] = -1;
		else			rst[i] = stack[top];
		
		stack[++top] = qst[i];
	}		
	
	for(i = 0; i < n; i++){
		printf("%d", rst[i]);
		if(i != n-1)	printf(" ");
	}
	
	return 0;
}
