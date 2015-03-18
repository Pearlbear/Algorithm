/*
  归并排序（数据结构与算法分析P175）;
*/
/*
  这个例程有一个问题在于每一个Merge函数会建立一个临时数组，同一时刻可能会有logN个数组存在，大大增加了空间开销，书上的例程好处在于永远只存在一个临时数组，节约了空间。

void MSort(int A[], int Left, int Right);
void Merge(int A[], int Lpos, int Rpos, int RightEnd);

void MergeSort(int A[], int N)
{
  MSort(A, 0, N-1);
}

void MSort(int A[], int Left, int Right)
{
  if(Left < Right)
    {
      int Center;
      Center = (Left + Right) >> 1;
      MSort(A, Left, Center);
      MSort(A, Center + 1, Right);
      Merge(A, Left, Center + 1, Right);
    }
}

void Merge(int A[], int Lpos, int Rpos, int RightEnd)
{
  int LeftEnd, N, TmpPos, i;
  LeftEnd = Rpos - 1;
  N = RightEnd - Lpos + 1;
  TmpPos = 0;
  int TmpArray[N];

  while(Lpos <= LeftEnd && Rpos <= RightEnd)
    {
      if(A[Lpos] < A[Rpos])
	TmpArray[TmpPos++] = A[Lpos++];
      else
	TmpArray[TmpPos++] = A[Rpos++];
    }
  while(Lpos <= LeftEnd)
    TmpArray[TmpPos++] = A[Lpos++];
  while(Rpos <= RightEnd)
    TmpArray[TmpPos++] = A[Rpos++];

  for(;N > 0 ; RightEnd--, N--)
      A[RightEnd] = TmpArray[N-1];
  free(TmpArray);
}
 */
void MSort(int A[], int TmpArray[], int Left, int Right);
void Merge(int A[], int TmpArray[], int Lpos, int Rpos, int RightEnd);

void MergeSort(int A[], int N)
{
  int TemArray[N];
  MSort(A, TemArray, 0, N-1);
}

void MSort(int A[], int TmpArray[], int Left, int Right)
{
  if(Left < Right)
    {
      int Center;
      Center = (Left + Right) >> 1;
      MSort(A, TmpArray, Left, Center);
      MSort(A, TmpArray, Center + 1, Right);
      Merge(A, TmpArray, Left, Center + 1, Right);
    }
}

void Merge(int A[], int TmpArray[], int Lpos, int Rpos, int RightEnd)
{
  int LeftEnd, N, TmpPos, i;
  LeftEnd = Rpos - 1;
  N = RightEnd - Lpos + 1;
  TmpPos = Lpos;

  while(Lpos <= LeftEnd && Rpos <= RightEnd)
    {
      if(A[Lpos] < A[Rpos])
	TmpArray[TmpPos++] = A[Lpos++];
      else
	TmpArray[TmpPos++] = A[Rpos++];
    }
  while(Lpos <= LeftEnd)
    TmpArray[TmpPos++] = A[Lpos++];
  while(Rpos <= RightEnd)
    TmpArray[TmpPos++] = A[Rpos++];

  for(;N > 0 ; RightEnd--, N--)
      A[RightEnd] = TmpArray[RightEnd];
}
