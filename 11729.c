/*
	hanoi(i, j, k, l)를 j줄에 있는 원판 i개를 k줄을 이용하여 l줄로 옮기는 함수라고 가정한다.
	i = 1, hanoi(1, 1, 2, 3) = 1
	i = 2, hanoi(2, 1, 2, 3) = hanoi(1, 1, 3, 2) + hanoi(1, 1, 2, 3) + hanoi(1, 2, 1, 3)
	i = 3, hanoi(3, 1, 3) = hanoi(2, 1, 3, 2) + hanoi(1, 1, 2, 3) + hanoi(2, 2, 1, 3)
	...
	i = n, hanoi(i, j, k, l) = hanoi(n-1, j, l, k) + hanoi(1, j, k, l) + hanoi(n-1, k, j, l)

*/

#include <stdio.h>

void hanoi(int i, int j, int k, int l){
	if(i == 1)	printf("%d %d\n", j, l);
	else{
		hanoi(i-1, j, l, k);
		hanoi(1, j ,k ,l);
		hanoi(i-1, k, j, l);
	}
}

int main(void){
	int i, n;
	int cnt[20];
	cnt[0] = 1;
	
	scanf("%d", &n);
	
	for(i = 1; i < n; i++){
		cnt[i] = cnt[0] + 2*cnt[i-1];
	}
	
	printf("%d\n", cnt[n-1]);
	
	hanoi(n, 1, 2, 3);
	
	return 0;
}
