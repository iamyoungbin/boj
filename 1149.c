#include <stdio.h>

int rst[2][3];
int temp[3];
int colIdx = 0;

int main()
{	
	int N;
	scanf("%d", &N);
	
	scanf("%d %d %d", &rst[colIdx][0], &rst[colIdx][1], &rst[colIdx][2]);
	
	int i;
	for(i = 0; i < N-1; i++){
		int lastIdx = colIdx;
		colIdx = colIdx == 0 ? 1 : 0;
		
		scanf("%d %d %d", &temp[0], &temp[1], &temp[2]);
		
		rst[colIdx][0] = temp[0] + (rst[lastIdx][1] < rst[lastIdx][2] ? rst[lastIdx][1] : rst[lastIdx][2]);
		rst[colIdx][1] = temp[1] + (rst[lastIdx][0] < rst[lastIdx][2] ? rst[lastIdx][0] : rst[lastIdx][2]);
		rst[colIdx][2] = temp[2] + (rst[lastIdx][0] < rst[lastIdx][1] ? rst[lastIdx][0] : rst[lastIdx][1]);
	}
	
	printf("%d\n", rst[colIdx][0] < rst[colIdx][1] ? 
	(rst[colIdx][0] < rst[colIdx][2] ? rst[colIdx][0] : rst[colIdx][2]) : (rst[colIdx][1] < rst[colIdx][2] ? rst[colIdx][1] : rst[colIdx][2]));
	
	return 0;
}
