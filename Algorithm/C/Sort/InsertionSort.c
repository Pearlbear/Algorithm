/*
  插入排序（数据结构与算法分析P166）
*/

void InsertionSort(int A[], int N)
{
  int i,j;
  int Tmp;
  for(i = 1; i < N; i++)
    {
      Tmp = A[i];
      for(j = i; j > 0 && A[j-1] > Tmp ;j--)
	A[j] = A[j-1];
      A[j] = Tmp;
    }
}
