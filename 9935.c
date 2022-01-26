#include <stdio.h>
#include <string.h>

char qt[1000002];	// question
char rst[1000002];	// result	1000000 + \n + \0
int rstIdx = -1;	// result index
char tgt[38];	//target		36 + \n + \0

char peek(int i){
	if(rstIdx-i <= -1) return '\0';
	
	return rst[rstIdx-i];
}

void pop(int i){
	rstIdx -= i;
}

void push(char c){
	rst[++rstIdx] = c;
}

int main(void){
	int i, j;
	
	fgets(qt, 1000002, stdin);
	fgets(tgt, 38, stdin);

	qt[strlen(qt)-1] = '\0';
	tgt[strlen(tgt)-1] = '\0';
	
	int qtLen = strlen(qt);
	int tgtLen = strlen(tgt);
	
	for(i = 0; i < qtLen; i++){
		if(qt[i] == tgt[tgtLen - 1]){
			for(j = 1; j < tgtLen; j++){
				if(peek(j-1) != tgt[tgtLen -1 - j])	break;
			}
			
			if(j == tgtLen)	pop(tgtLen - 1);
			else			push(qt[i]);					
		}
		else{
			push(qt[i]);
		}
	}
	
	if(rstIdx == -1)	printf("FRULA");
	else{
		for(i = 0; i <= rstIdx; i++)	printf("%c", rst[i]);
	}
	
	return 0;
}
