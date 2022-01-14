/*

	baekjoon online judge
	No. 1158
	
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int item;
	struct Node* next;
}Node;

void Josephus(Node* head, int k){
	Node* cur = head;
	Node* tar = NULL;
	printf("<");
	int i = k-1;
	while(!(head->item == 1)){
		while(i--){
			cur = cur->next;
		}
		
		i = k-1;
		tar = cur->next;
		printf("%d, ", tar->item);
		cur->next = tar->next;
		free(tar);
		head->item--;
	}
	cur = cur->next;	// k=1 인 경우, list size = 1 이여도 cur = head 이기 때문에. 
	printf("%d>\n", cur->item);
	free(cur);
}

void MakeList(Node* head, int n){
	int i;
	Node* cur = head;
	for(i = 1; i <= n; i++){
		Node* temp = (Node*)malloc(sizeof(Node));
		temp->item = i;
		temp->next = NULL;
		
		cur->next = temp;
		cur = cur->next;
		
		head->item++;
	}
	
	cur->next = head->next;
}

int main(void){
	int n, k;
	
	Node* head = (Node*)malloc(sizeof(Node));
	head->item = 0;
	head->next = NULL;
	
	scanf("%d %d", &n, &k);
	
	MakeList(head, n);
	Josephus(head, k);
	
	free(head);
	
	return 0;
}
