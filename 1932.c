#include <stdio.h>

int arr[2][500];
int temp;
int row = 0;

int main()
{
	int N;
	scanf("%d", &N);
	
	scanf("%d", &arr[row][0]);
	
	int i;
	for(i = 1; i < N; i++){
		int preRow = row;
		row = row == 0 ? 1 : 0;
		
		int j;
		for(j = 0; j <= i; j++){
			scanf("%d", &temp);
			
			if(j == 0){
				arr[row][j] = temp + arr[preRow][j];
				continue;
			}
			if(j == i){
				arr[row][j] = temp + arr[preRow][j-1];
				continue;
			}
			
			arr[row][j] = temp + (arr[preRow][j] > arr[preRow][j-1] ? arr[preRow][j] : arr[preRow][j-1]);		
		}
	}
	
	int rst = 0;
	for(i = 0; i < N; i++){
		if(arr[row][i] > rst)	rst = arr[row][i];
	}
	
	printf("%d\n", rst);
	
	return 0;
}
