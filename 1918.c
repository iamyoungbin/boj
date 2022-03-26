#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char stack[100];
int top = -1;
char cmd[102];

void Push(char c)
{
	stack[++top] = c;
}

void Pop()
{
	printf("%c", stack[top--]);
}

char Peek()
{
	if(top == -1)	return '#';
	return stack[top];
}

int Priority(char c)
{
	switch(c){
		case '(' : 				return 0;
		case '+' : case '-' :	return 1;
		case '*' : case '/' :	return 2;
		default :				return -1;
	}
}

int main(void)
{
	char cmd[102];
	fgets(cmd, 102, stdin);
	
	int i;
	for(i = 0; i < strlen(cmd)-1; i++){
		switch(cmd[i]){
			case '(' :
				Push(cmd[i]);
				break;
			case ')' :
				while(Peek() != '('){
					Pop();
				}
				top--;
				break;
			case '+' : case '-' : case '*' : case '/' :
				while(Priority(cmd[i]) <= Priority(Peek())){
					Pop();
				}				
				
				Push(cmd[i]);
				break;			
			default :
				printf("%c", cmd[i]);
				break;
		}
	}
	
	while(top != -1){
		printf("%c", stack[top--]);
	}

}
