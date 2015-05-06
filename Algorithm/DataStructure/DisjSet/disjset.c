void Initialize( DisjSet S )
{
  int i;

  for(i = NumSets; i > 0; i--)
      S[i] = 0;
}

void SetUnion( DisjSet S, SetType Root1, SetType Root2 )
{
  /*
    常规式
    S[Root2] = Root1;
  */
  /*
    按高度
  */
  if(S[Root1] < S[Root2])
    S[Root2] = Root1;
  else
    {
      if(S[Root1] == S[Root2])
	S[Root2]--;
      S[Root1] = Root2;
    }
}


SetType Find( ElementType X, DisjSet S )
{
  if(S[X] <= 0)
    return X;
  else
    /*常规式
      return Find(S[X], S);
    */
    /*
      路径压缩
     */
    return S[X] = Find(S[X], S);
}
