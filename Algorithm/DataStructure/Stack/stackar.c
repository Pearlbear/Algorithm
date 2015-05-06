/*
  栈的数组实现
*/

#define EmptyTOS (-1)
#define MinStackSize (5)

struct StackRecord
{
  int TopOfStack;
  int Capacity;
  ElementType *Array;
};

Stack CreateStack( int MaxElements )
{
  Stack S;
  if(MaxElements < MinStackSize)
    Error("栈空间太小");
  S = malloc(sizeof(struct StackRecord));
  if(S == NULL)
    FatalError("未分配空间");

  S->Array = malloc(sizeof(ElementType) * MaxElements);
  if(S->Array == NULL)
    FatalError("未分配空间");
  S->Capacity = MaxElements;
  MakeEmpty(S);

  return S;
}

/*
  用不着用if(!IsEmpty(S))......Pop(S)...
  因为用不着清空栈里面的元素，空间已经分配了，就算清空也不能释放空间，当下次再需要该空间时，会自动覆盖已有元素
*/
void MakeEmpty( Stack S )
{
  S->TopOfStack = EmptyTOS;
}
/*
  释放栈
*/
void DisposeStack( Stack S )
{
  if(S != NULL)
    {
      free(S->Array);
      free(S);
    }
}

int IsEmpty( Stack S )
{
  return S->TopOfStack == EmptyTOS;
}

void Push( ElementType X, Stack S )
{
  if(IsFull(S))
    Error("栈已满");
  else
    S->Array[++S->TopOfStack] = X;
}

ElementType Top( Stack S )
{
  if(IsEmpty(S))
    {
      Error("空栈");
      return 0;
    }
  return S->Array[S->TopOfStack];
}

void Pop( Stack S )
{
  if(IsEmpty(S))
    Error("空栈");
  else
    S->TopOfStack--;
}

ElementType TopAndPop( Stack S )
{
  if(!IsEmpty(S))
    return S->Array[S->TopOfStack--];
  Error("空栈");
  return 0;
}
