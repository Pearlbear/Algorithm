struct AvlNode
{
  ElementType Element;
  AvlTree Left;
  AvlTree Right;
  int Height;
};

static int Height(AvlTree T)
{
  if(T == NULL)
    return -1;
  else
    return T->Height;
}

AvlTree Insert( ElementType X, AvlTree T )
{
  if(T == NULL)
    {
      T = malloc(sizeof(struct AvlNode));
      if(T == NULL)
	FatalError("未分配空间");
      else
	{
	  T->Element = X;
	  T->Left = T->Right = NULL;
	  T->Height = 0;
	}
    }
  else
    {
      if(X < T->Element)
	{
	  T->Left = Insert(X, T->Left);
	  if(Height(X->Left) - Height(X->Right) ==2)
	    if(X < T->Left->Element)
	      SingleRotateWithLeft(T);
	    else
	      DoubleRotateWithLeft(T);
	}
      else if(X > T->Element)
	{
	  T->Right = Insert(X, T->Right);
	  if(Height(X->Right) - Height(X->Left) ==2)
	    if(X > T->Right->Element)
	      SingleRotateWithRight(T);
	    else
	      DoubleRotateWithRight(T);
	}
    }
  T->Height = Max(Height(T->Left), Height(T->Right)) + 1;
  return T;
}

static Position SingleRotateWithLeft(Position K2)
{
  Position K1;
  K1 = K2->Left;
  K2->Left = K1->Right;
  K1->Right = K2;
  K2->Height = Max(Height(K2->Left), Height(K2->Right)) + 1;
  K1->Height = Max(Height(K1->Left), K2->Height) + 1;
  return K1;
}

static Position DoubleRotateWithLeft(Position K3)
{
  /*
  Position K1,K2;
  K1 = K3->Left;
  K2 = K1->Right;
  K3->Left = K2->Right;
  K1->Right = K2->Left;
  K2->Left = K1;
  K2->Right = K3;
  K1->Height = Max(Height(K1->Left), Height(K1->Right)) + 1;
  k3->Height = Max(Height(K3->Left), Height(K3->Right)) + 1;
  K2->Height = Max(K1->Height, K3->Height) + 1;
  return K2;
  */
  //我真是无语……直接两个单旋转可以解决的问题……
  K3->Left = SingleRotateWithRight(K3->Left);
  return SingleRotateWithLeft(K3);
}
