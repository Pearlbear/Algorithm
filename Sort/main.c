#include <stdio.h>
#include <time.h>
#include "InsertionSort.c"
#include "ShellSort.c"
#include "HeapSort.c"

void InsertionSort(int A[], int N);
void ShellSort(int A[], int N);
void HeapSort(int A[], int N);

int main()
{
  //生成随机数列
  int length;
  length = 1000;
  int a[length],b[length];
  int i; 
  srand((unsigned)time(NULL));

  for(i = 0; i < length; i++)
    {
      a[i] = rand(100)%(1000-1);
      printf("%d ", a[i]);
    }
  for(i = 0; i < length; i++)
    b[i] = a[i];
  printf("\n");
  
  //算法一时间
  int time;
  /* time = clock(); */
  
  /* InsertionSort(a, length); */
  /* /\* for(i = 0; i < length; i++) *\/ */
  /* /\*   { *\/ */
  /* /\*     printf("%d ", a[i]); *\/ */
  /* /\*   } *\/ */
  /* printf("\n"); */
  /* time = clock() - time; */
  /* printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC); */

  //算法二时间
  time = clock();
  
  ShellSort(a, length);
  /* for(i = 0; i < length; i++) */
  /*   { */
  /*     printf("%d ", a[i]); */
  /*   } */
  printf("\n");
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);

  //算法三时间
  time = clock();
  
  HeapSort(b, length);
  /* for(i = 0; i < length; i++) */
  /*   { */
  /*     printf("%d ", b[i]); */
  /*   } */
  printf("\n");
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
}
