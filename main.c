#include <stdio.h>
#include <time.h>//clock()
main(){
  int presentTime;
  presentTime = clock();
  
  

  presentTime = clock() - presentTime;
  printf("It took %ds ticks (%f seconds).\n", presentTime, ((double)presentTime)/CLOCKS_PER_SEC);
}
