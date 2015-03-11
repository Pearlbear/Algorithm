struct TreeNode
{
  ElementType Element;
  PriorityQueue Left;
  PriorityQueue Right;
  int Npl
};

PriorityQueue Merge( PriorityQueue H1, PriorityQueue H2 )
{
  if(H1 == NULL)
    return H2;
  if(H2 == NULL)
    return H1;
  if(H1->Element < H2->Element)
    return Merge1(H1, H2);
  else
    return Merge1(H2, H1);
}
/*
  Weiss真实人才
*/
static PriorityQueue Merge1(PriorityQueue H1, PriorityQueue H2)
{
  if(H1->Left == NULL)
    H1->Left = H2;
  else
    {
      H1->Right = Merge(H1->Right, H2);
      if(H1->Left->Npl < H1->Right->Npl)
	SwapChildren(H1);
      H1->Npl = H1->Right->Npl + 1;
    }
  return H1;
}

static SwapChildren(PriorityQueue H)
{
  PriorityQueue TmpCell;
  TmpCell = H->Left;
  H->Left = H->Right;
  H->Right = TmpCell;
}

ElementType FindMin( PriorityQueue H )
{
  return H->Element;
}

PriorityQueue Insert1( ElementType X, PriorityQueue H )
{
  PriorityQueue NewCell;
  NewCell = malloc(sizeof(struct TreeNode));
  if(NewCell == NULL)
    FatalError("未分配空间");
  else
    {
      NewCell->Left = NewCell->Right = NULL;
      NewCell->Element = X;
      NewCell->Npl = 0;
    }
  return Merge(NewCell, H);
}
ElementType DeleteMin( PriorityQueue H)
{
  ElementType MinElement;
  MinElement = FindMin(H);
  H = DeleteMin1(H);
  return MinElement;
}

PriorityQueue DeleteMin1( PriorityQueue H )
{
  PriorityQueue LeftHeap,RightHeap;
  if(IsEmpty(H))
    {
      Error("空堆");
      return NULL;
    }
  LeftHeap = H->Left;
  RightHeap = H->Right;
  free(H);
  return Merge(LeftHeap, RightHeap);
}
