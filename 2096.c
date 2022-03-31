#include <stdio.h>

int max[2][3];
int min[2][3];

int column = 0;

int GetMax(int a, int b, int c)
{
	if(a > b){
		if(a > c)	return a;
		else		return c;
	}
	else{
		if(b > c)	return b;
		else		return c;
	}
}

int GetMin(int a, int b, int c)
{
	if(a < b){
		if(a < c)	return a;
		else		return c;
	}
	else{
		if(b < c)	return b;
		else		return c;
	}
}

int main(void)
{
	int N;
	scanf("%d", &N);
	
	int i;
	for(i = 0; i < 3; i++){
		scanf("%d", &max[column][i]);
		min[column][i] = max[column][i];
	}
	
	int j;
	for(i = 1; i < N; i++){
		int curCol = column;
		column = column==0 ? 1 : 0;
		
		for(j = 0; j < 3; j++){
			int temp;
			scanf("%d", &temp);
			
			switch(j){
				case 0 : 
					max[column][0] = max[curCol][0] > max[curCol][1] ? max[curCol][0] + temp : max[curCol][1] + temp;
					min[column][0] = min[curCol][0] < min[curCol][1] ? min[curCol][0] + temp : min[curCol][1] + temp;
					break;
				case 1 :
					max[column][1] = GetMax(max[curCol][0], max[curCol][1], max[curCol][2]) + temp;
					min[column][1] = GetMin(min[curCol][0], min[curCol][1], min[curCol][2]) + temp;
					break;
				case 2 :
					max[column][2] = max[curCol][2] > max[curCol][1] ? max[curCol][2] + temp : max[curCol][1] + temp;
					min[column][2] = min[curCol][2] < min[curCol][1] ? min[curCol][2] + temp : min[curCol][1] + temp;
					break;
			}
		}
	}
	
	int maxValue = max[column][0];
	int minValue = min[column][0];
	
	for(i = 1; i < 3; i++){
		if(maxValue < max[column][i])	maxValue = max[column][i];
		if(minValue > min[column][i])	minValue = min[column][i];
	}
	
	printf("%d %d", maxValue, minValue);
	
	return 0;
}
