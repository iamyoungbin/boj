#include <stdio.h>
#include <string.h>

typedef struct queue{
	int seq[300000];
	int front;
	int rear;
}queue;

queue q[19];	// len : 2 ~ 20

int main(void){
	int n, k;
	
	long long cnt = 0;
	char buf[22];
	int len;
		
	scanf("%d %d", &n, &k);
	
	int i;
	
	for(i = 0; i < 19; i++){
		q[i].front = -1;
		q[i].rear = -1;	// 생각좀 해보자... 
	}	
	
	for(i = 0; i < n; i++){
		scanf("%s", buf);
		len = strlen(buf) - 2;	// len - '\n' - (len 1 -> index 0)
		
		if(q[len].front == q[len].rear){
			q[len].rear++;
			q[len].seq[q[len].rear] = i;	// enqueue
			//printf("enqueue q[len].rear : q[%d].%d, seq : i,,, because of front == rear\n", len, q[len].rear, i);
		}
		else{
			while(i - q[len].seq[q[len].front + 1] > k){
				//printf("dequeue q[len].front : q[%d].%d, seq : i,,,\n", len, q[len].front);
				q[len].front++;	// dequeue
				
				if(q[len].front == q[len].rear)	break;
			}
			
			q[len].rear++;
			q[len].seq[q[len].rear] = i;	// enqueue			
			//printf("enqueue q[len].rear : q[%d].%d, seq : i,,,\n", len, q[len].rear, i);
			
			cnt += (long long)(q[len].rear - q[len].front - 1);	// q[len].rear에 대한 쌍을 더하기 위함으로 -1 연산( q[len].rear 를 추가로 쌍으로 계산하지 않기 위해.) 
			//printf("cnt : %lld... + %d\n", cnt, q[len].rear - q[len].front - 1);
		}
	}
	
	printf("%lld", cnt);
	
	return 0;
}
