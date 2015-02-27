/*
  求X的N次方（数据结构与算法分析P23）
*/
#include <stdio.h>
int main()
{
  int X,N;
  printf("Enter the X:");
  scanf("%d",&X);
  printf("Enter the N:");
  scanf("%d",&N);
  int result = Pow(X,N);
  printf("%d power of %d is: %d.\n",N ,X ,result);
  return 0;
}
/*
  算法一：
  分算法
  算法时间复杂度：O(logN)
  参数：X，N次方
*/
int Pow(int X, int N)
{
  if(N == 0)
    return 1;
  if(N % 2 == 0)
    return Pow(X*X, N/2);
  else
    return X * Pow(X, N-1);
}
