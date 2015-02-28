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
  
}

Position FindPrevious(List L, ElementType X)
{
  Position P;
  P = L->Next;
}
