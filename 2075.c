#include <stdio.h>

#define N_MAX_SIZE	1500

typedef struct Heap{
	int element[N_MAX_SIZE+1];
	int heapSize;
}HeapType;

void InitHeap(HeapType *heap)
{
	heap->heapSize = 0;
}

void InsertHeap(HeapType *heap, int key)
{
	int i = ++(heap->heapSize);
	
	while((i != 1) && (key < heap->element[i/2])){
		heap->element[i] = heap->element[i/2];
		i /= 2;
	}
	
	heap->element[i] = key;
}

void DeleteHeap(HeapType *heap)
{
	int rst, temp;
	rst = heap->element[1];
	temp = heap->element[(heap->heapSize)--];
	
	int parent, child;
	parent = 1;
	child = 2;
	
	while(child <= heap->heapSize){
		if((child < heap->heapSize) && (heap->element[child+1] < heap->element[child]))	child++;
		if(temp < heap->element[child])	break;
		
		heap->element[parent] = heap->element[child];
		parent = child;
		child *= 2;
	}
	heap->element[parent] = temp;
}

int main(void)
{
	int N;
	scanf("%d", &N);
	
	HeapType heap;
	InitHeap(&heap);
	
	int i, j;
	for(i = 0; i < N; i++){
		for(j = 0; j < N; j++){
			int temp;
			scanf("%d", &temp);
			getchar();
			
			if(heap.heapSize < N)	InsertHeap(&heap, temp);
			else if(heap.element[1] < temp){
				DeleteHeap(&heap);
				InsertHeap(&heap, temp);
			}
		}
	}
	
	int rst = heap.element[1];
	
	printf("%d\n", rst);
	return 0;
}
