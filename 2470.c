#include <stdio.h>
#include <stdlib.h>

int sol[100000];

int Compare(const void* first, const void* second)
{
	if(*(int*)first > *(int*)second)	return 1;
	if(*(int*)first < *(int*)second)	return -1;
										return 0;
}

int main(void)
{
	int N;
	scanf("%d", &N);
	
	int left = 0;
	int right = N-1;

	int i;
	for(i = 0; i < N; i++){
		scanf("%d", &sol[i]);
	}
	
	qsort(sol, N, sizeof(int), Compare);
	
	int min = 2000000001;
	int ls, rs;
	
	while(!(left == right || min == 0)){
		int temp = sol[left] + sol[right];
		
		if(abs(temp) < min){
			min = abs(temp);
			ls = left;
			rs = right;
		}
		if(temp > 0){
			right--;
		}
		else{
			left++;
		}
	}
	
	/*
	for(i = 0; i < N; i++){
		printf("%d ", sol[i]);
	}
	printf("\n");
	*/
	
	printf("%d %d\n", sol[ls], sol[rs]);
	
	return 0;
}
