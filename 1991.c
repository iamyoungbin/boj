#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	char item;
	struct Node* left;
	struct Node* right;
}Node;

Node* MakeNode(char c)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->item = c;
	newNode->left = newNode->right = NULL;
	
	return newNode;
}

Node* SearchNode(Node* root, char c)
{
	if(root != NULL){
		if(root->item == c)	return root;
		else{
			Node* temp = SearchNode(root->left, c);
			if(temp != NULL)	return temp;
			return SearchNode(root->right, c);
		}
	}
	
	return NULL;
}

void InsertNode(Node* p, char l, char r)
{
	if(l != '.'){
		Node* ln = MakeNode(l);
		p->left = ln;
	}
	
	if(r != '.'){
		Node* rn = MakeNode(r);
		p->right = rn;
	}	
}

void FreeTree(Node* root)
{
	if(root == NULL)	return;
	
	FreeTree(root->left);
	FreeTree(root->right);
	free(root);
}

void Preorder(Node* root)
{
	if(root == NULL)	return;
	
	printf("%c", root->item);
	
	Preorder(root->left);
	Preorder(root->right);
}

void Inorder(Node* root)
{
	if(root == NULL)	return;
	
	Inorder(root->left);
	printf("%c", root->item);
	Inorder(root->right);
}

void Postorder(Node* root)
{
	if(root == NULL)	return;
	
	Postorder(root->left);
	Postorder(root->right);
	printf("%c", root->item);
}

int main(void)
{
	int  N;
	scanf("%d", &N);
	getchar();
	
	Node* root = MakeNode('A');
	Node* parent;
	
	int i;
	for(i = 0; i < N; i++){
		char n, l, r;	// now, left, right
		scanf("%c %c %c", &n, &l, &r);
		getchar();
		
		parent = SearchNode(root, n);
		
		InsertNode(parent, l, r);
	}
	
	Preorder(root);
	printf("\n");
	Inorder(root);
	printf("\n");
	Postorder(root);
	printf("\n");
	
	FreeTree(root);
	
	return 0;
}
