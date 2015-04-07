/*
 * @author: Psyche
 * time complexity: 
 */
#include <math.h>
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
}
