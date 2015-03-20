/*
  求第k个最大（最小）元（数据结构与算法分析P186）
 */
#include <stdio.h>
#include <time.h>
#include "InsertionSort.c"

#define true (1)
#define Cutoff (3)

int QuickSelect(int A[], int k, int N);
void Qselect(int A[], int k, int Left, int Right);
int Median3(int A[], int Left, int Right);
void Swap(int *a, int *b);

int main()
{
  //生成随机数列
  int length;
  int k;
  length = 100;
  k = 51;
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

  //答案
  InsertionSort(a, length);
  int Answer;
  Answer = a[k-1];
  printf("The answer is %d\n", Answer);
  //算法一时间
  int time;
  time = clock();

  int Result;
  Result = QuickSelect(b, k, length);
  /* for(i = 0; i < length; i++) */
  /*   { */
  /*     printf("%d ", a[i]); */
  /*   } */
  printf("The %dth number is: %d\n", k, Result);
  
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
}
/*
  算法一：
  快速选择
  算法时间复杂度：O(N)
  参数：目标数组，第k个数，数组大小
 */

int QuickSelect(int A[], int k, int N)
{
  Qselect(A, k-1, 0, N-1);
  return A[k-1];
}

void Qselect(int A[], int k, int Left, int Right)
{
  if(Right - Left >= Cutoff)
    {
      int Pivot;
      int i,j;
      Pivot = Median3(A, Left, Right);
      i = Left;
      j = Right - 1;
      while(true)
	{
	  while(A[++i] < Pivot){}
	  while(A[--j] > Pivot){}
	  if(i < j)
	    Swap(&A[i], &A[j]);
	  else
	    break;
	}
      Swap(&A[i], &A[Right - 1]);
      //这个位置跟书上稍微有点儿区别，书上的例程我认为有点儿问题，但也有可能是取决于Quicksort例程的调用参数
      if(k < i)
	Qselect(A, k, Left, i-1);
      else if(k > i)
	Qselect(A, k, i+1, Right);
    }
  else
    InsertionSort(A + Left, Right - Left + 1);
}

/*
  选取中值数，参见QuickSort
 */
int Median3(int A[], int Left, int Right)
{
  int Middle;
  Middle = (Left + Right) >> 1;
  if(A[Left] > A[Right])
    Swap(&A[Left], &A[Right]);
  if(A[Left] > A[Middle])
    Swap(&A[Left], &A[Middle]);
  if(A[Middle] > A[Right])
    Swap(&A[Middle], &A[Right]);

  Swap(&A[Middle], &A[Right - 1]);
  return A[Right - 1];
}

void Swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}
