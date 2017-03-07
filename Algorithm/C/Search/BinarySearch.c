/*
  二分查找
  书上的例程有个问题在于如果查找目标有多个，不能返回第一个目标
 */
int BinarySearch(int A[], int X, int N)
{
  int Low, Mid, High;
  Low = 0;
  High = N - 1;
  while(Low <= High)
    {
      Mid = (Low + High) >> 1;
      /*
	//我的：
      if(X <= A[Mid])
      	High = Mid;
      else
      	Low = Mid + 1;
      if(Low == High && X == A[Mid])
	return Mid;
      if(Low == High)
	break;
      */
      //书上的：
      if(A[Mid] < X)
	Low = Mid + 1;
      else if(A[Mid] > X)
	High = Mid - 1;
      else
	return Mid;
    }
  return -1;
}
