struct HeapStruct
{
  int Size;
  int Capacity;
  ElementType *Elements;
};

PriorityQueue Initialize( int MaxElements )
{
  if(MaxElements < MinPQSize)
    Error("声明的优先队列太小");
  PriorityQueue Q;
  Q = malloc(sizeof(struct HeapStruct));
  if(Q == NULL)
    FatalError("未分配空间");
  Q->Size = 0;
  Q->Capacity = MaxElements;
  Q->Elements = malloc(sizeof(ElementType)*(Q->Size+1));
  if(Q->Elements == NULL)
    FatalError("未分配空间");
  Q->Elements[0] = MinData;
  return Q;
}

void Insert( ElementType X, PriorityQueue H )
{
  int i;
  if(IsFull(H))
    {
      Error("优先队列已满");
      return;
    }
  for(i = ++H->Size;X < *(H->Elements + i/2);i/=2)
    *(H->Elements + i) = *(H->Elements + i/2);
  *(H->Elements + i) = X;
}

ElementType DeleteMin( PriorityQueue H )
{
  int i;
  ElementType MinElement,LastElement;
  if(IsEmpty(H))
    {
      Error("空优先队列");
      return H->Elements[0];
    }
  MinElement = H->Elements[1];
  LastElement = H->Elements[H->Size--];
  for(i = 1;i*2 < H->Size;)
    {
      MinChild = H->Elements[2*i] < H->Elements[2*i+1] ? 2*i : 2*i+1;
      if(LastElement > H->Elements[MinChild])
	{
	  H->Elements[i] = H->Elements[MinChild];
	  i = MinChild;
	}
      else
	{
	  H->Elements[i] = LastElements;
	  break;
	}
    }
  return MinElement;
}
