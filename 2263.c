#include <stdio.h>

#define MAX_N_SIZE	100000

int in[MAX_N_SIZE];
int post[MAX_N_SIZE];

void PreOrder(int root, int start, int end)
{
	printf("%d ", post[root]);
	
	if(start != end){
		int i = start;
		while(post[root] != in[i] && i <= end)	i++;
		
		if(i == start)	PreOrder(root-1, i+1, end);		// only right subtree
		else if(i == end)	PreOrder(root-1-end+i, start, i-1);	// only left subtree
		
		else{
			PreOrder(root-1-end+i, start, i-1);	// left subtree
			PreOrder(root-1, i+1, end);			// right subtree
		}
	}
}

int main(void)
{
	int n;
	scanf("%d", &n);
	
	int i;
	for(i = 0; i < n; i++){
		scanf("%d", &in[i]);
	}
	for(i = 0; i < n; i++){
		scanf("%d", &post[i]);
	}
	
	PreOrder(n-1, 0, n-1);
	
	return 0;
}
