/*

	baekjoon online judge
	No. 5397

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node{
	char item;
	struct Node* prev;
	struct Node* next;
}Node;

Node* InsertNode(Node* cur, char c){
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->item = c;
	
	if(cur->next != NULL){
		cur->next->prev = newNode;
		newNode->next = cur->next;
	}
	else	newNode->next = NULL;
	
	cur->next = newNode;
	newNode->prev = cur;
	
	return cur->next;
}

Node* RemoveNode(Node* n){
	Node* delNode = n;
	Node* cur = n;
	
	if(delNode->item != '\0'){
		cur = cur->prev;
		if(delNode->next != NULL){
			cur->next = delNode->next;
			delNode->next->prev = cur;
		}
		else cur->next = NULL;
		
		free(delNode);
	}
	
	return cur;
}

void RemoveList(Node* h){
	Node* delNode;
	Node* trail = h->next;
	
	while(trail){
		delNode = trail;
		trail = trail->next;
		
		free(delNode);
	}
	
	h->next = NULL;
}

void PrintList(Node* h){
	Node* temp = h->next;
	while(temp){
		printf("%c", temp->item);
		temp = temp->next;
	}
	printf("\n");
}

int main(void){
	int n;
	char c;
	Node* head = (Node*)malloc(sizeof(Node));
	head->item = '\0';
	head->prev = NULL;
	head->next = NULL;
	Node* cur = head;
	
	scanf("%d\n", &n);
	while(n--){
		while((c = getchar()) != '\n'){
			switch(c){
				case '-' :
					cur = RemoveNode(cur);
					break;
				case '<' :
					if(cur->prev != NULL)	cur = cur->prev;
					break;
				case '>' :
					if(cur->next != NULL)	cur = cur->next;
					break;
				default : 
					cur = InsertNode(cur, c);
			}
		}
		
		PrintList(head);
		RemoveList(head);
		cur = head;
	}
	
	free(head);
	
	return 0;
}
