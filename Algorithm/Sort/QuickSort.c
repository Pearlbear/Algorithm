/*
  快速排序（数据结构与算法分析P181）;
*/
//#include "InsertionSort.c"

#define Cutoff (10)//对于小数组使用插入排序
#define true (1)

void Qsort(int A[], int Left, int Right);
int Median3(int A[], int Left, int Right);

void QuickSort(int A[], int N)
{
  Qsort(A, 0, N-1);
}

void Qsort(int A[], int Left, int Right)
{
  if(Right - Left < Cutoff)
      InsertionSort(A+Left, Right - Left + 1);
  else
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
      Qsort(A, Left, i-1);
      Qsort(A, i+1, Right);
    }
}

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

  Swap(&A[Middle], &A[Right - 1]);//将中值数放在Right-1位置上，而不是Right位置，因为Right位置已经大于中值了
  return A[Right - 1];
}
/*
static void Swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}
*/
