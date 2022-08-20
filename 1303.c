#include <stdio.h>

#define WHITE	1
#define BLUE	2

int map[100][100];
int visited[100][100] = {0, };

int M, N;
int dm[4] = {1, -1, 0, 0};
int dn[4] = {0, 0, -1, 1};

int sum = 0;
int wp = 0, bp = 0;

void dfs(int m, int n)
{
	sum++;
	visited[m][n] = 1;
	
	int i;
	for(i = 0; i < 4; i++){
		int nm = m + dm[i];
		int nn = n + dn[i];
		
		if(nm >= 0 && nm < M && nn >= 0 && nn < N){
			if(!visited[nm][nn] && map[m][n] == map[nm][nn])
				dfs(nm, nn);
		}
	}
}

int main(void)
{
	scanf("%d %d", &N, &M);
	getchar();
	
	int i, j;
	for(i = 0; i < M; i++){
		for(j = 0; j < N; j++){
			char c;
			scanf("%c", &c);
			if(c == 'W')	map[i][j] = WHITE;
			else			map[i][j] = BLUE;
		}
		getchar();
	}	
		
	for(i = 0; i < M; i++){
		for(j = 0; j < N; j++){
			if(!visited[i][j]){
				dfs(i, j);
				if(map[i][j] == WHITE)	wp += sum*sum;
				else					bp += sum*sum;
			}	
			sum = 0;
		}
	}
	
	printf("%d %d\n", wp, bp);
	
	return 0;
}
