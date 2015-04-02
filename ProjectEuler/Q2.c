/*
 * @author: Psyche
 * @description: 
 * @time complexity: 
 */
/*
int SumOfEvenFibonacci(int limit)
{
  int Last, SecLast, Answer, Sum;
  SecLast = 1;
  Last = 2;
  Sum = Last;
  Answer = SecLast + Last;
  while(Answer <= limit)
    {
      if(!(Answer % 2))
	Sum += Answer;
      SecLast = Last;
      Last = Answer;
      Answer = SecLast + Last;
      printf("sum=%d ", Sum);
    }
  return Sum;
}*/

/*
 * @author: Euler
 * @description: 
 * @time complexity: 
 */
int SumOfEvenFibonacci(int limit)
{
  int Last, SecLast, Answer, Sum;
  SecLast = 2;
  Last = 8;  
  Sum = Last + SecLast;
  Answer = 4*Last + SecLast;
  while(Answer <= limit)
    {
      Sum += Answer;
      SecLast = Last;
      Last = Answer;
      Answer = 4*Last + SecLast;
    }
  return Sum;
}
