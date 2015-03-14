
static void swap(int A[],int i,int j);

void ShellSort(int A[], int N)
{
  int Increment,i,j;
  int Tmp;
  for(Increment = N/2; Increment > 0; Increment/=2)
    {
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

static void swap(int A[],int i,int j)
{
  A[i] = A[i] ^ A[j];
  A[j] = A[i] ^ A[j];
  A[i] = A[i] ^ A[j];
}
