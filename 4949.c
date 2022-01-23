#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SIZE 100

int stack[MAX_SIZE];
int top = -1;

void push(char c){
	stack[++top] = c;
}

char peek(){
	if(top == -1) return '.';
	return stack[top];
}

bool Compare(char c1, char c2){
	if(c1 == ']' && c2 == '[')	return true;
	if(c1 == ')' && c2 == '(')	return true;
	
	return false;
}

int main(void){
	int i;
	char str[102];
	
	while(1){
		fgets(str, 101, stdin);
		top = -1;
		bool sol = true;
		if((str[0] == '.') && str[1] == '\n')	break;
		
		for(i = 0; str[i] != '\0'; i++){
			if(sol == false) break;
			
			switch(str[i]){
				case '(' :
					push(str[i]);
					break;
				case '[' :
					push(str[i]);
					break;
				case ')' :
					if(Compare(str[i], peek()))	top--;
					else						sol = false;
					break;
				case ']' : 
					if(Compare(str[i], peek()))	top--;
					else						sol = false;
			}
		}
		
		if(top != -1)	sol = false;
		
		if(sol) printf("yes\n");
		else	printf("no\n");
	}
	
	return 0;
}
