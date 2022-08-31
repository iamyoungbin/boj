#include <stdio.h>

#define MAX_MAP_SIZE    125
#define INF 100000

int map[MAX_MAP_SIZE][MAX_MAP_SIZE];
int dist[MAX_MAP_SIZE][MAX_MAP_SIZE];
int visited[MAX_MAP_SIZE][MAX_MAP_SIZE];

typedef struct Point{
    int y;
    int x;
}Point;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

Point choose(int n)
{
    int i, j, min = INF;
    Point p;
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(dist[i][j] < min && !visited[i][j]){ // ���� �湮���� �ʰ� ��ΰ� ���� ª�� ��� ��ȯ
                min = dist[i][j];
                p.y = i;
                p.x = j;
            }
        }
    }

    return p;
}

int dijkstra(int n)
{
    int next = n;
    int i, j;
    for(i = 0; i < n; i++){ // �ʱ�ȭ
        for(j = 0; j < n; j++){
            dist[i][j] = INF;
            visited[i][j] = 0;
        }
    }
    dist[0][0] = map[0][0];

    for(i = 0; i < n*n; i++){
        Point v = choose(n);
        visited[v.y][v.x] = 1;  // �湮 ǥ��

        for(j = 0; j < 4; j++){ // �̿� ���� �����¿� �� ���
            int ny = v.y + dy[j];
            int nx = v.x + dx[j];

            if(ny >= 0 && ny < n && nx >= 0 && nx < n && !visited[ny][nx]){
                if(dist[v.y][v.x] + map[ny][nx] < dist[ny][nx]) // ���� ��κ��� ���� �湮 ��忡���� ��ΰ� �� ª����
                    dist[ny][nx] = dist[v.y][v.x] + map[ny][nx];    // ��� ����ġ ��ü
            }
        }

    }
    /*
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            printf("%5d ", dist[i][j]);
        }
        printf("\n");
    }
    */

    return dist[n-1][n-1];
}

int main()
{
    int cnt = 1;

    while(1){
        int N;
        scanf("%d", &N);
        if(N == 0)  break;

        int i, j;
        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++){
                scanf("%d", &map[i][j]);
            }
        }

        printf("Problem %d: %d\n", cnt, dijkstra(N));

       cnt++;
    }

    return 0;
}