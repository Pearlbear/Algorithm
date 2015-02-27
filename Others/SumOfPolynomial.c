/*
  求多项式的值（数据结构与算法分析P28练习2.10）
*/
#include <stdio.h>
#include <time.h>
int Pow_B(int,int);

int main()
{
  int X = 2;
  int length = 20;
  int A[length];
  int i; 
  srand((unsigned)time(NULL));
  for(i = 0; i < length; i++){
    A[i] = rand()%100;
    printf("%d ", A[i]);
  }
  printf("\n");
  
  //算法一时间
  int time;
  time = clock();
  
  int sum1;
  sum1 = SumOfPolynomial_A(A, X,length);
  printf("Sum=%d\n", sum1);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  
  ////算法二时间
  time = clock();
  
  int sum2;
  sum2 = SumOfPolynomial_B(A, X,length);
  printf("Sum=%d\n", sum2);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  return 0;
}

/*
  算法一：
  直接相加
  算法时间复杂度：O(N^2)
  参数：多项式系数A[]，X
*/
int SumOfPolynomial_A(int A[], int X, int length)
{
  int sum = 0;
  int i,j;
  for(i = 0;i < length; i++)
    {
      sum = sum + A[i]*Pow_B(X,i);
    }
  return sum;
}
/*
  算法二：
  Horner法则
  算法时间复杂度：O(N)
  参数：多项式系数A[]，X
*/
int SumOfPolynomial_B(int A[], int X, int length)
{
  int sum = 0;
  int i;
  for(i = length -1;i >= 0;i--)
    {
      sum = sum * X + A[i];
    }
  return sum;
}
