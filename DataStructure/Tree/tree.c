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
	T->Left = Insert(X, T->Left); //第一个T->Left有待商榷，因为这样永远都返回的整棵树，而不知道X插入的具体位置，如果要返回具体位置的话应该写T
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
  Position P,BeforeP,AfterP;
  BeforeP = T;
}
