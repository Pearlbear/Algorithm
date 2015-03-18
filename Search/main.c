#include <stdio.h>
#include <time.h>
#include "InsertionSort.c"
#include "BinarySearch.c"

void InsertionSort(int A[], int N);
int BinarySearch(int A[], int X, int N);

int main()
{
  //生成随机数列
  int length;
  length = 100;
  int a[length];
  int i; 
  srand((unsigned)time(NULL));

  for(i = 0; i < length; i++)
    a[i] = 55;//rand(100)%(1000-1);
  InsertionSort(a, length);
  for(i = 0; i < length; i++)
      printf("%d ", a[i]);
  printf("\n");
  
  //算法一时间
  int time;
  int Position;
  time = clock();

  Position = BinarySearch(a, 55, length);
  printf("The number u find is on %d.", Position);
  printf("\n");
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  
  return 0;
}

