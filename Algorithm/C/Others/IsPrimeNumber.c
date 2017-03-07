/*
  求多项式的值（数据结构与算法分析P28练习2.10）
*/
#include <stdio.h>
#include <math.h>

int main()
{
  int N;
  int boolean;
  printf("Please enter a number to know if it's a prime number: ");
  scanf("%d", &N);
  boolean = IsPrime_A(N);
  if(boolean)
    printf("%d is a prime number.\n", N);
  else
    printf("%d is not a prime number.\n", N);
}

/*
  算法一：
  能否除尽从3到N的1/2次方间的奇数
  算法时间复杂度：O(N^1/2)
  参数：N
*/
int IsPrime_A(int N)
{
  if(N < 1)
    return 0;
  if(N == 1)
    return 0;
  if(N == 2)
    return 1;
  if(N%2==0)
    return 0;
  int i;
  int limit = sqrt((double)N);
  for(i = 3;i < limit;i += 2)
    {
      if(N%i==0)
	return 0;
    }
  return 1;
}
