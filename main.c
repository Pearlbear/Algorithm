#include <stdio.h>
#include <time.h>//clock()
#include "MaxSubSequenceSum.c"

main(){
  int a[100];
  int i; 
  srand((unsigned)time(NULL));
  for(i = 0; i < 100; i++){
    a[i] = rand(100)%(100-1)-49;
    printf("%d ", a[i]);
  }
  printf("\n");
  
  //用于统计时间
  int time;
  time = clock();
  
  int sum1;
  sum1 = MaxSubSequenceSum_A(a, 100);
  printf("Sum=%d\n", sum1);

  //用于统计时间
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  
  time = clock();
  
  int sum2;
  sum2 = MaxSubSequenceSum_B(a, 100);
  printf("Sum=%d\n", sum2);

  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);

  return 0;
}

