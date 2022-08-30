#include <stdio.h>
#include <math.h>

#define MAX_N_SIZE  100
#define INF 3000

typedef struct Point{
    float x;
    float y;
}Point;

Point star[MAX_N_SIZE];
float dist[MAX_N_SIZE];
int selected[MAX_N_SIZE] = {0, };

int getNextVertex(int n)
{
    int v, i, min = INF;
    for(i = 0; i < n; i++){
        if(!selected[i] && dist[i] < min){
            min = dist[i];
            v = i;
        }
    }

    return v;
}

float prim(int s, int n) // start vertex, total vertex number
{
    dist[s] = 0.0;
    float sum = 0.0;

    int i;
    for(i = 0; i < n; i++){
        int v = getNextVertex(n);
        sum += dist[v];
        selected[v] = 1;

        int j;
        for(j = 0; j < n; j++){
            if(v != j && !selected[j]){
                float temp = sqrt(pow(star[v].x - star[j].x, 2) + pow(star[v].y - star[j].y, 2));
                if(temp < dist[j])
                    dist[j] = temp;
            }
        }
    }

    return sum;
}

int main()
{
    int n;
    scanf("%d", &n);

    int i;
    for(i = 0; i < n; i++){
        scanf("%f %f", &star[i].x, &star[i].y);
        dist[i] = INF;
    }

    printf("%f\n", prim(0, n));

    return 0;
}