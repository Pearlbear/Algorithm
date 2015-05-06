/*
 * @author: Psyche
 * time complexity: O(N)
 */
/*
int SumOfMultipleOfThreeAndFive(int limit)
{
  int i,sum;
  sum = 0;
  for(i = 1; i < 1000; i++)
      if(i%3 == 0 || i%5 == 0)
	sum += i;
  return sum;
}*/

/*
 * @author: Euler
 * time complexity: O(1)
 */
static int SumOfDivisibleBy(int divisor, int limit)
{
  int n = (limit - 1) / divisor;
  return n * (1 + n)/2 * divisor;
}
int SumOfMultipleOfThreeAndFive(int limit)
{
  return SumOfDivisibleBy(3, limit) + SumOfDivisibleBy(5, limit) - SumOfDivisibleBy(15, limit);
}

