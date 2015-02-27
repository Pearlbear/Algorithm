/*
  求X的N次方（数据结构与算法分析P23）
*/
#include <stdio.h>
/* int main() */
/* { */
/*   int X,N; */
/*   printf("Enter the X:"); */
/*   scanf("%d",&X); */
/*   printf("Enter the N:"); */
/*   scanf("%d",&N); */
/*   int result = Pow(X,N); */
/*   printf("%d power of %d is: %d.\n",N ,X ,result); */
/*   return 0; */
/* } */
/*
  算法一：
  分算法
  算法时间复杂度：O(logN)
  参数：X，N次方
*/
int Pow_A(int X, int N)
{
  if(N == 0)
    return 1;
  if(N % 2 == 0)
    return Pow_A(X*X, N/2);
  else
    return X * Pow_A(X, N-1);
}
/*
  算法二：
  直接相乘
  算法时间复杂度：O(N)
  参数：X，N次方
*/
int Pow_B(int X, int N)
{
  int pow = 1;
  int i;
  for(i = 0;i < N; i++)
    {
      pow = pow * X;
    }
  return pow;
}
