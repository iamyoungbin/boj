#include <stdio.h>

#define MAX_SIZE	50

int map[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE];

int hv[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int wv[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

int w, h;

void dfs(int ph, int pw)
{
	visited[ph][pw] = 1;
	
	int i;	
	for(i = 0; i < 8; i++){
		int nh = ph + hv[i];
		int nw  = pw + wv[i];
		
		if(!visited[nh][nw] && map[nh][nw] == 1 && nh >= 0 && nw >= 0 && nh < h && nw < w)
			dfs(nh, nw);
	}
}

int main(void)
{	
	while(1){
		int cnt = 0;
		
		scanf("%d %d", &w, &h);
		if(w == 0 && h == 0)	return 0;
		
		int i, j;
		for(i=0; i < h; i++){
			for(j=0; j < w; j++){
				scanf("%d", &map[i][j]);
				visited[i][j] = 0;
			}		
		}
		
		for(i = 0; i < h; i++){
			for(j = 0; j < w; j++){
				if(map[i][j] == 1 && !visited[i][j]){
					cnt++;
					dfs(i, j);
				}
			}
		}
		
		printf("%d\n", cnt);
	}
	
	return 0;
}
