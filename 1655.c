#include <stdio.h>

#define MAX_N_SIZE	100001

typedef struct HeapType{
	int tree[MAX_N_SIZE];
	int size;
}HeapType;

HeapType maxH, minH;

void InitHeap()
{
	maxH.size = minH.size = 0;
}

int Peek(HeapType *h)
{
	if(h->size != 0)	return h->tree[1];
}

void PushMax(int value)
{
	maxH.tree[++(maxH.size)] = value;
	
	int i = maxH.size;
	while(i != 1){
		if(maxH.tree[i] > maxH.tree[i/2]){
			int temp = maxH.tree[i];
			maxH.tree[i] = maxH.tree[i/2];
			maxH.tree[i/2] = temp;
			
			i /= 2;
		}
		else	break;
	}	
}

void PushMin(int value)
{
	minH.tree[++(minH.size)] = value;
	
	int i = minH.size;
	while(i != 1){
		if(minH.tree[i] < minH.tree[i/2]){
			int temp = minH.tree[i];
			minH.tree[i] = minH.tree[i/2];
			minH.tree[i/2] = temp;
			
			i /= 2;
		}
		else	break;
	}
}

int PopMax()
{
	int tgt = maxH.tree[1];
	int temp = maxH.tree[(maxH.size)--];
	
	int child = 2, parent = 1;
	
	while(child <= maxH.size){
		if(child < maxH.size && maxH.tree[child] < maxH.tree[child+1])	child++;
		
		if(temp < maxH.tree[child]){
			maxH.tree[parent] = maxH.tree[child];
		
			parent = child;
			child *= 2;	
		}
		else	break;
	}
	
	maxH.tree[parent] = temp;
	return tgt;
}

int PopMin()
{
	int tgt = minH.tree[1];
	int temp = minH.tree[(minH.size)--];
	
	int child = 2, parent = 1;
	
	while(child <= minH.size){
		if(child < minH.size && minH.tree[child] > minH.tree[child+1])	child++;
		
		if(temp > minH.tree[child]){
			minH.tree[parent] = minH.tree[child];
		
			parent = child;
			child *= 2;	
		}
		else	break;
	}
	
	minH.tree[parent] = temp;
	return tgt;
}

int main()
{
	InitHeap();
	
	int N;
	scanf("%d", &N);
	
	int max, min;
	
	int i, value, v2;
	for(i = 0; i < N; i++){
		switch(i){
			case 0 :
				scanf("%d", &value);
				printf("%d\n", value);
				//printf("** %d\n", value);
				break;
				
			case 1 :
				scanf("%d", &v2);
				if(v2 > value){
					int temp = value;
					value = v2;
					v2 = temp;
				}
		
				PushMin(value);
				PushMax(v2);
		
				printf("%d\n", Peek(&maxH));	
				//printf("** %d\n", Peek(&maxH));			
				break;
				
			default :	// maxHeap : e_1 ~~~~~ e_i, minHeap : e_i+1 ~~~~~~~ e_N	===> target = e_i
				scanf("%d", &value);
			
				if(value > Peek(&minH))	PushMin(value);
				else					PushMax(value);
				
				// minHeap_size <= maxHeap_size <= minHeap_size + 1
				if(maxH.size - minH.size > 1){	// case : minHeap_size + 1 < maxHeap_size 
					value = PopMax();
					PushMin(value);
				}
				else if(minH.size - maxH.size > 0){	// case : minHeap_size > maxHeap_size
					value = PopMin();
					PushMax(value);
				}
				
				printf("%d\n", Peek(&maxH));	
				//printf("** %d\n", Peek(&maxH));	
		}
	}
	
	return 0;
}
