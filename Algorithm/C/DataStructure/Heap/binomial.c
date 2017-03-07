struct BinNode
{
  ElementType Element;
  BinTree NextSibling;
  BinTree Child;
};

struct Collection
{
  int CurrentSize;
  BinTree TheTrees[MaxTrees];
};

BinTree CombineTrees(BinTree T1, BinTree T2)
{
  if(T1->Element > T2->Element)
    return CombineTrees(T2, T1);
  T2->NextSibling = T1->Child;
  T1->Child = T2;
  return T1;
}

BinQueue Merge(BinQueue H1, BinQueue H2)
{
  if((H1->CurrentSize + H2->CurrentSize) > Capacity)
    Error("超出范围");
  H1->CurrentSize += H2->CurrentSize;

  BinTree T1, T2, Carry;
  int i,j;
  for(i = 0, j = 1;j <= H1->CurrentSize; i++, j << 1)
    {
      T1 = H1->TheTrees[i];
      T2 = H2->TheTrees[i];
      switch(!!T1 + 2*!!T2 + 4*!!Carry) //使用了类似linux权限管理的数学方法
	{
	case 0:
	case 1:
	  break;
	case 2:
	  H1->TheTrees[i] = T2;
	  H2->TheTrees[i] = NULL;
	  break;
	case 4:
	  H1->TheTrees[i] = Carry;
	  Carry = NULL;
	  break;
	case 3:
	  Carry = CombineTrees(T1, T2);
	  H1->TheTrees[i] = H2->TheTrees[i] = NULL;
	  break;
	case 5:
	  Carry = CombineTrees(T1, Carry);
	  H1->TheTrees[i] = NULL;
	  break;
	case 6:
	  Carry = CombineTrees(T2, Carry);
	  H2->TheTrees[i] = NULL;
	  break;
	case 7:
	  H1->TheTrees[i] = Carry;
	  Carry = CombineTrees(T1, T2);
	  H2->TheTrees[i] = NULL;
	  break;
	}
    }
  return H1;
}

ElementType DeleteMin(BinQueue H)
{
  if(H == NULL)
    {
      Error("H是空队列");
      return NULL;
    }
  ElementType MinElement;
  int i;
  int MinTree;
  BinTree DeletedTree, OldRoot;
  Binqueue DeletedQueue;
  
  MinElement = Infinity;
  for( i = 0; i < MaxTrees; i++)
    {
      if(H->TheTrees[i] && H->TheTrees[i]->Element < MinElement)
	{
	  MinElement = H->TheTrees[i]->Element;
	  MinTree = i;
	}
    }
  DeletedTree = H->TheTrees[MinTree];
  H->TheTrees[MinTree] = NULL;
  OldRoot = DeletedTree;
  DeletedTree = DeletedTree->Child;
  free(OldRoot);

  DeletedQueue = InitialQueue();
  DeletedQueue->CurrentSize = (1 << MinTree) - 1;
  for( i = MinTree - 1; i >= 0; i--)
    {
      DeletedQueue->TheTrees[i] = DeletedTree;
      DeletedTree = DeletedTree->NextSibling;
      DeletedQueue->TheTrees[i]->NextSibling = NULL;
    }
  H->CurrentSize -= (DeletedQueue->CurrentSize + 1);
  Merge(H, DeletedQueue);
  return MinElement;
}
