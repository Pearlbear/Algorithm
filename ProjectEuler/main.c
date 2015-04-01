#include <stdio.h>
#include <time.h>

#include "Q1.c"

int SumOfMultipleOfThreeAndFive(int limit);

int main()
{
  int time;
  int sum;
  time = clock();
  sum = SumOfMultipleOfThreeAndFive(1000);
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  printf("sum = %d\n", sum);
}
