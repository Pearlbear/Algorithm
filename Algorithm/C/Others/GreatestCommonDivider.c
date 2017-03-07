/*
  求最大公因数（数据结构与算法分析P23）
*/
#include <stdio.h>
int main()
{
  int a,b;
  printf("Enter the first number:");
  scanf("%d",&a);
  printf("Enter the second number:");
  scanf("%d",&b);
  int result = GCD(a,b);
  printf("The greatest common divider of %d and %d is %d.\n",a,b,result);
  return 0;
}
/*
  算法一：
  欧几里德算法
  算法时间复杂度：O(logN)
  参数：求公约数的两个数
*/
int GCD(int a,int b)
{
  int tmp;
  while(b!=0)
    {
      tmp = a%b;
      a = b;
      b = tmp;
    }
  return a;
}
