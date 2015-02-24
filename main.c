#include <stdio.h>
#include <time.h>//clock()
#include "MaxSubSequenceSum.c"

main(){
  //用于统计时间
  int time;
  time = clock();

  //用于统计时间
  time = clock() - time;
  printf("It took %ds ticks (%f seconds).\n", time, ((double)time)/CLOCKS_PER_SEC);
  
  return 0;
}

