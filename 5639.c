#include <stdio.h>

#define NODE_MAX_SIZE	10000

int tree[NODE_MAX_SIZE];
int n = 0;

void PostOrder(int root, int start, int end)
{
	int sep = start;	// separator
	if(root != end){
		while(sep <= end){
			if(tree[root] < tree[sep])	break;
			
			sep++;
		}
		
		if(start != sep){	// left subtree
			PostOrder(start, start+1, sep-1);
		}
	
		if(end != sep-1){	// right subtree
			PostOrder(sep, sep+1, end);
		}
	}
	
	printf("%d\n", tree[root]);
}

int main(void)
{
	int value;
	while(scanf("%d", &value) != EOF){
		tree[n++] = value;
	}
	
	PostOrder(0, 1, n-1);
	
	return 0;
}
