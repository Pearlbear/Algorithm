#include <stdio.h>
/*
  求最大子序列和
*/

/*
  算法一：
  遍历所有子序列和
  算法时间复杂度：O(N^3)
*/
int MaxSubSequenceSum_A(int A[], int N)
{
  int MaxSum, ThisSum, i, j, k;
  MaxSum = 0;
	
  for(i = 0; i < N; i++)
    {
      for(j = i; j < N; j++)
	{
	  ThisSum = 0;
	  for(k = i; k <= j; k++)
	    {
	      ThisSum += A[k];
	    }
	  if(ThisSum > MaxSum)
	    MaxSum = ThisSum;
	}
    }
	
  return MaxSum;
}
/*
  算法二：
  也是遍历所有子序列和，不过改进了子序列和计算效率
  算法时间复杂度：O(N^2)
*/
int MaxSubSequenceSum_B(int A[], int N){
  int MaxSum, ThisSum, i,j;
  MaxSum = 0;

  for(i = 0;i < N; i++)
    {
      ThisSum = 0;
      for(j = i;j < N; j++)
	{
      	  ThisSum += A[j];
	  if(ThisSum > MaxSum)
	    MaxSum = ThisSum;
	}
    }
  return MaxSum;
}
