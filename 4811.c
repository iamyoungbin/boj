#include <stdio.h>

long long date[31][31] = {0, };

long long Pill(int w, int h)
{
	if(date[w][h] != 0)	return date[w][h];
	if(w == 0){
		date[w][h] = 1;
		return date[w][h];
	}
	if(w == h){
		date[w][h] = Pill(w-1, h);
		return date[w][h];
	}
	
	date[w][h] = Pill(w-1, h) + Pill(w, h-1);
	return date[w][h];
}

int main(void)
{
	while(1){
		int N;
		scanf("%d", &N);
		if(N == 0)	break;
		
		printf("%lli\n", Pill(N, N));
	}
	
	return 0;
}
