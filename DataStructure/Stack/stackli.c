struct Node
{
  ElementType Element;
  PtrToNode Next;
};

int IsEmpty(Stack S)
{
  return S->Next == Null;
}

Stack CreateStack(void)
{
  Stack S;
  S = malloc(sizeof(struct Node));
  if(S == NULL)
    FatalError("未分配空间");
  S->Next = NULL;
  MakeEmpty(S);//才分配的空间，怎么可能不为空？
  return S;
}

void MakeEmpty(Stack S)
{
  if(S == NULL)
    Error("S == NULL");
  else
    while(!IsEmpty(S))
      Pop(S);
}

void Push(ElementType X, Stack S)
{
  PtrToNode TmpCell;
  TmpCell = malloc(sizeof(struct Node));
  if(TmpCell == NULL)
    FatalError("未分配空间");
  else
    {
      TmpCell->Element = X;
      TmpCell->Next = S->Next;
      S->Next = TmpCell;
    }
}

ElementType Top(Stack S)
{
  if(!IsEmpty(S))
    return S->Next->Element;
  Error("空栈");
  return 0;
}

void Pop(Stack S)
{
  if(IsEmpty(S))
    {
      Error("空栈");
      return;
    }
  PtrToNode TmpCell;
  TmpCell = S->Next;
  S->Next = TmpCell->Next;
  free(TmpCell);
}
