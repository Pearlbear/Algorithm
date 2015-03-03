struct TreeNode
{
  ElementType Element;
  SearchTree Left;
  SearchTree Right;
};

/*
  为什么返回值要是SearchTree？既然都return NULL，不如直接返回void？
 */
SearchTree MakeEmpty( SearchTree T )
{
  if(T != NULL)
    {
      MakeEmpty(T->Left);
      MakeEmpty(T->Right);
      free(T);
    }
  return NULL;
}

Position Find( ElementType X, SearchTree T )
{
  if(T == NULL)
    return NULL;
  if(X > T->Element)
    return Find (X, T->Right);
  else if(X < T->Element)
    return Find(X, T->Left);
  else
    return T;
}

/*
  此处用递归不大合适，因为对同一个节点进行了两次判定，浪费！
 */
Position FindMin( SearchTree T )
{
  if(T == NULL)
    return NULL;
  else if(T->Left != NULL)
    return FindMin(T->Left);
  else
    return T;
}
/*
  巧妙之处在于当T为NULL时就直接返回了NULL，不用写return NULL了
 */
Position FindMax( SearchTree T )
{
  if(T != NULL)
    while(T->Right != NULL)
      T = T->Right;
  return T;
}

SearchTree Insert( ElementType X, SearchTree T )
{
  if(T != NULL)
    {
      if(X < T->Element)
	T->Left = Insert(X, T->Left); //第一个T->Left不能写成T！！否则整棵树将只剩一个节点
      else if(X > T->Element)
        T->Right = Insert(X, T->Right); //同上
    }
  else
    {
      T = malloc(sizeof(struct TreeNode));
      if(T == NULL)
	error("未分配空间");
      else
	{
	  T->Element = X;
	  T->Left = T->Right = NULL;
	}
    }
  return T;
}

SearchTree Delete( ElementType X, SearchTree T )
{
  if(T != NULL )
    {
      if(X < T->Element)
	T->Left = Delete(X, T->Left);
      else if(X > T->Element)
	T->Right = Delete(X, T->Right);
      else
	{
	  Position P;
	  if(T->Left != NULL && T->Right != NULL)
	    {
	      /*这个地方效率稍微有点儿低，因为进行了两次查找最小值，可以重新写个既删除又返回最小值的DeleteMin函数来代替
	      P = FindMin(T->Right);
	      T->Element = P->Element;
	      T->Right = Delete(T->Element, T->Right);
	      */
	      P = DeleteMin(T->Right);
	    }
	  else
	    {
	      P = T;
	      if(T->Right == NULL) //这个位置的巧妙之处在于直接包含了左右都为空的处理
		T = T->Left;
	      else if(T->Left == NULL)
		T = T->Right;
	      free(P);
	    }
	}
    }
  return T;
}
/*
  增加Delete函数效率的函数，有点儿问题，暂无法使用
 */
/*
static ElementType DeleteMin(SearchTree T)
{
  Position BeforeP,P,AfterP;
  ElementType Min;
  BeforeP = T;
  if(BeforeP != NULL)
    {
      if((P = BeforeP->Left) != NULL)
	{
	  while(P->Left != NULL)
	    {
	      BeforeP = BeforeP->Left;
	      P = BeforeP->Left;
	    }
	  Min = P->Element;
	  AfterP = P->Right;
	  BeforeP->Left = AfterP;
	  free(P);
	}
      else
	{
	  Min = BeforeP->Element;
	  
	}
    }
  else
    Min = NULL;
  return Min;
}
*/
