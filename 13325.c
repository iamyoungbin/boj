#include <stdio.h>
#include <math.h>

#define MAX_SIZE	(1 << 21)

/*
	***
	test case :
	3
	1 2 1 3 2 4 2 1 1 1 1 1 1 2
	***
*/

int tree[MAX_SIZE];
int n;

long long sum = 0;

int dfs(int p)
{
	int c1, c2;
	if(p*2 > n){
		sum += tree[p];
		return tree[p];
	}
	else{
		c1 = dfs(p*2);
		c2 = dfs(p*2 + 1);
		
		int g = c1 - c2;
		if(g > 0){
			tree[p*2 + 1] += g;
		}
		else{
			g *= -1;
			tree[p*2] += g;
		}
		sum += g;
	}
	sum += tree[p];
	
	return c1>c2 ? tree[p]+c1 : tree[p]+c2;
}

int main(void)
{
	int k;
	scanf("%d", &k);
	n = (int)pow(2.0, (double)(k+1)) - 1;
	tree[1] = 0;
	
	int i;
	for(i = 2; i <= n; i++)	scanf("%d", &tree[i]);
	
	dfs(1);
	printf("%lld\n", sum);
	
	return 0;
}
