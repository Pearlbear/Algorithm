struct Node
{
  ElementType Element;
  Postion Next;
};

List MakeEmpty(List L)
{
  
}

int IsEmpty(List L)
{
  return L->Next == NULL;
}

int IsLast(Position P, List L)
{
  return P->Next == NULL;
}

/*
  这个例程很巧妙的在于当没有找到时会直接返回NULL
 */
Position Find(List L, ElementType X)
{
  Position P;
  P = L->Next;
  while(P != NULL && P->Element != X)
    {
      P = P->Next;
    }
  return P;
}

void Delete(List L, ElementType X)
{
  Postion P, TmpCell;
  P = FindPrevious(L, X);
  if(!IsLast(P, L))
    {
      TmpCell = P->Next;
      P->Next = TmpCell->Next;
      free(TmpCell);
      TmpCell = NULL;//是否加上这句会好些？还是在画蛇添足？把TmpCell里面存储的地址也删除掉？还是会自动删除
    }
}

Position FindPrevious(List L, ElementType X)
{
  Position P;
  P = L;
  while(P->Next != NULL && P->Next->Element != X)
    P = P->Next;
  return P;
}

void Insert(ElementType X, List L, Position P)
{
  Position TmpCell;
  TmpCell = malloc(sizeof(struct Node));
  if(TmpCell == NULL)
    FatalError("未分配空间");
  TmpCell->Element = X;
  TmpCell->Next = P->Next;
  P->Next = TmpCell;
}
/*
  书上的MakeEmpty和DeleteList不是在做同一件事吗？MakeEmpty调用了DeleteList，此时L->Next已经指向NULL，这时又重新开辟空间，重新让L->Next指向NULL？有何意义？
 */
void DeleteList(List L)
{
  Position P, TmpCell;
  P = L;
  while(P!=Null)
    {
      TmpCell = P->Next;
      free(P);
      P = TmpCell;
    }
}
