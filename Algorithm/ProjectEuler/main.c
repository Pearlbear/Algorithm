#include <stdio.h>
#include <time.h>


#include "Q1.c"
#include "Q2.c"
#include "Q3.c"

//int SumOfMultipleOfThreeAndFive(int limit);
//int SumOfEvenFibonacci(int limit);
int LargestPrimeFactor(long long N);

int main()
{
  //Q1
  /*
  int sum;
  int time;
  time = clock();

  sum = SumOfMultipleOfThreeAndFive(1000);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  printf("sum = %d\n", sum);
  */

  //Q2
  /*
  int sum;
  int time;
  time = clock();

  sum = SumOfEvenFibonacci(4000000);
  
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  printf("sum = %d\n", sum);
  */

  //Q3
  int largestPrimeFactor;
  int time;
  time = clock();

  largestPrimeFactor = LargestPrimeFactor(600851475143);
  
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  printf("LargestPrimeFactor = %d\n", largestPrimeFactor);
  
}
