#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node{
	char item;
	struct Node *prev;
	struct Node *next;
}Node;

void InsertNode(Node* n, char c){
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->item = c;
	newNode->next = NULL;
	
	if(n->next != NULL){
		n->next->prev = newNode;
		newNode->next = n->next;
	}
	
	n->next = newNode;
	newNode->prev = n;
}

void RemoveNode(Node* delNode){
	if(delNode->item != '@'){
		if(delNode->next != NULL){
			delNode->prev->next = delNode->next;
			delNode->next->prev = delNode->prev;
		}
		else{
			delNode->prev->next = NULL;
		}
		free(delNode);		
	}
}

void PrintList(Node* h){
	Node* temp = h->next;
	while(temp){
		printf("%c", temp->item);
		temp = temp->next;
	}
}

int main(void){

	Node* head = (Node*)malloc(sizeof(Node));
	head->item = '@';
	head->prev = NULL;
	head->next = NULL;
	
	Node* cur = head;
	char c;
	
	while((c = getchar()) != '\n'){
		InsertNode(cur, c);
		cur = cur->next;	
	}
	
	int i, cn;
	char cmd[10];

	scanf("%d", &cn);
	getchar();
	for(i = 0; i < cn; i++){
		fgets(cmd, 10, stdin);		
		switch(cmd[0]){
			case 'L' : 
				if(cur->prev != NULL) cur = cur->prev;
				break;
			case 'D' :
				if(cur->next != NULL) cur = cur->next;
				break;
			case 'B' :
				if(cur->prev != NULL){
					cur = cur->prev;
					RemoveNode(cur->next);
				}
				break;
			case 'P' : 
				InsertNode(cur, cmd[2]);
				cur = cur->next;
				break;
			default :
				printf("Error...\n");
		}
	}
	
	PrintList(head);
	
	cur = head->next;
	while(cur != NULL){
		Node* temp = cur;
		cur = cur->next;
		RemoveNode(temp);
	}
	free(head);
	
	return 0;
}
