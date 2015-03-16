/*
  希尔排序（数据结构与算法分析P168）;
*/
void ShellSort(int A[], int N)
{
  int Increment,i,j;
  int Tmp;
  for(Increment = N/2; Increment > 0; Increment/=2)
    {
      //相当于一个间隔为Increment的插入排序
      for(i = Increment; i < N; i++)
	{
	  Tmp = A[i];
	  for(j = i;j >= Increment && Tmp < A[j-Increment];j-=Increment)
	    A[j] = A[j-Increment];
	  A[j] = Tmp;
	}
    }
  printf("\n");
}
