/*
  堆排序（数据结构与算法分析P172）;
*/
#define LeftChild(i) (2*(i)+1)

static void PercolateDown(int A[], int i, int N);
static void Swap(int *a, int *b);

void HeapSort(int A[], int N)
{
  int i;
  for(i = N/2;i >= 0;i--)//其实就等于每插入一个数上滤，但是这样可以减少一半的开销
    PercolateDown(A, i, N);
  for(i = N-1; i > 0; i--)
    {
      Swap(&A[i], &A[0]);
      PercolateDown(A, 0, i);
    }
}

static void PercolateDown(int A[], int i, int N)
{
  int Child;
  int Tmp;
  for(Tmp = A[i];LeftChild(i) < N;i = Child)
    {
      Child = LeftChild(i);
      if(Child < N-1 && A[Child] < A[Child+1])
	Child++;
      if(Tmp < A[Child])
	A[i] = A[Child];
      else
	break;
    }
  A[i] = Tmp;
}

static void Swap(int *a, int *b)
{
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}
