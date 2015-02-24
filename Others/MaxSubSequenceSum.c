#include <stdio.h>
#include <time.h>
/*
  求最大子序列和（数据结构与算法分析2.4.3）
*/
main(){
  //生成长度为100的随机数列
  int a[100];
  int i; 
  srand((unsigned)time(NULL));
  for(i = 0; i < 100; i++){
    a[i] = rand(100)%(100-1)-49;
    printf("%d ", a[i]);
  }
  printf("\n");
  
  //算法一时间
  int time;
  time = clock();
  
  int sum1;
  sum1 = MaxSubSequenceSum_A(a, 100);
  printf("Sum=%d\n", sum1);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  
  //算法二时间
  time = clock();
   
  int sum2;
  sum2 = MaxSubSequenceSum_B(a, 100);
  printf("Sum=%d\n", sum2);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  
  //算法三时间
  time = clock();

  int sum3;
  sum3 = MaxSubSequenceSum_C(a, 100);
  printf("Sum=%d\n", sum3);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);

  //算法四时间
  time = clock();
  
  int sum4;
  sum4 = MaxSubSequenceSum_D(a, 100);
  printf("Sum=%d\n", sum4);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  return 0;
}
/*
  算法一：
  遍历所有子序列和
  算法时间复杂度：O(N^3)
  参数：
  A[]：目标数组
  N：数组长度
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
int MaxSubSequenceSum_B(int A[], int N)
{
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
/*
  算法三：
  分治法，采用递归形式
  算法时间复杂度：O(N*logN)
*/
int MaxSum(int A[], int Left, int Right)
{
  int Middle, i;
  int MaxLeftSum, MaxRightSum;
  int MaxLeftBorderSum, MaxRightBorderSum;
  int LeftBorderSum, RightBorderSum;
  if(Left>=Right)
    {
      return A[Left];
    }
  Middle = (Left + Right) >> 1;
  
  MaxLeftSum = MaxSum(A, Left, Middle);
  MaxRightSum = MaxSum(A, Middle+1, Right);
  
  MaxLeftBorderSum = 0;
  LeftBorderSum = 0;
  for(i = Middle; i >= Left; i--)
    {
      LeftBorderSum += A[i];
      if(LeftBorderSum > MaxLeftBorderSum)
	{
	  MaxLeftBorderSum = LeftBorderSum;
	}
    }
  
  MaxRightBorderSum = 0;
  RightBorderSum = 0;
  for(i = Middle + 1; i <= Right; i++)
    {
      RightBorderSum += A[i];
      if(RightBorderSum > MaxRightBorderSum)
	{
	  MaxRightBorderSum = RightBorderSum;
	}
    }

  int MaxSum = MaxLeftBorderSum + MaxRightBorderSum;
  int temp = (MaxLeftSum > MaxRightSum) ? MaxLeftSum : MaxRightSum;
  return (MaxSum > temp)? MaxSum : temp;
}

int MaxSubSequenceSum_C(int A[], int N)
{
  return MaxSum(A, 0, N-1);
}

/*
  算法四：
  线性算法
  算法时间复杂度：O(N)
*/
int MaxSubSequenceSum_D(int A[], int N)
{
  int ThisSum, MaxSum, i;
  ThisSum = MaxSum = 0;
  for(i = 0; i < N; i++)
    {
      ThisSum += A[i];
      if(ThisSum > MaxSum)
	MaxSum = ThisSum;
      else if(ThisSum < 0)
	ThisSum = 0;
    }
  return MaxSum;
}
