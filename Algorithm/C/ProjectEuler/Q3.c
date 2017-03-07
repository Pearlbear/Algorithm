/*
 * @author: Psyche
 * time complexity: 
 */
/*
int isPrime(int N)
{
  int i;
  if(N<2)
    return 0;
  if(N==2)
    return 1;
  if(N==3)
    return 1;
  if(!(N%2))
    return 0;
  for(i = 3;i < N/2;i+=2)
    {
      if(!(N%i))
	return 0;
    }
  return 1;
}
int LargestPrimeFactor(long long N)
{
  int i;
  while(!(N%2))
    N = N >> 1;
  for(i = 3;i <= N/2;i+=2)
    {
      if(isPrime(i))
	while(!(N%i))
	  N /= i;
    }
  return N;
}*/

/*
 * @author: Euler
 * time complexity: 
 */
#include <math.h>
int LargestPrimeFactor(long long N)
{
  if(N<2)
    return -1;
  int LargestFactor,Factor,MostFactor;
  if(!(N%2))
    {
      LargestFactor = 2;
      while(!(N%2))
	N /= 2;
    }
  Factor = 3;
  MostFactor = (int)sqrt((long double)N);
  while(N > 1 && Factor < MostFactor)
    {
      if(!(N%Factor))
	{
	  LargestFactor = Factor;
	  while(!(N%Factor))
	    N/=Factor;
	  MostFactor = (int)sqrt((long double)N);//这一步很重要，极大节约时间
	}
      Factor+=2;
    }
  if(N > 1)
    return N;
  else
    return LargestFactor;
} 
