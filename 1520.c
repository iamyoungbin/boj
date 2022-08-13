#include <stdio.h>

#define MAX_SIZE	500

int map[MAX_SIZE][MAX_SIZE];
int course[MAX_SIZE][MAX_SIZE];

int M, N;
int dm[4] = {-1, 1, 0, 0};
int dn[4] = {0, 0, -1, 1};

int dfs(int pm, int pn)
{
	if(pm == M-1 && pn == N-1){
		course[pm][pn] = 1;
		return 1;
	}
	if(course[pm][pn] != -1)	return course[pm][pn];
	
	int i, cnt = 0;
	for(i = 0; i < 4; i++){
		int nm = pm + dm[i];
		int nn = pn + dn[i];
	
		if(nm >= 0 && nm < M && nn >= 0 && nn < N && map[pm][pn] > map[nm][nn]){
			cnt += dfs(nm, nn);
		}
	}
	
	course[pm][pn] = cnt;	
	
	return course[pm][pn];
}

int main(void)
{
	scanf("%d %d", &M, &N);
	
	int i, j;
	for(i = 0; i < M; i++){
		for(j = 0; j < N; j++){
			int temp;
			scanf("%d", &temp);
			map[i][j] = temp;
			course[i][j] = -1;
		}
	}
	
	printf("%d\n", dfs(0, 0));
	
	return 0;
}
