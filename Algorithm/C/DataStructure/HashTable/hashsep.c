struct ListNode
{
  ElementType Element;
  Position Next;
};

struct HashTbl
{
  int TableSize;
  List *TheLists;
};

HashTable InitializeTable( int TableSize )
{
  HashTable H;
  int i;
  if(TableSize < MinTableSize)
    {
      Error("散列表太小");
      return NULL;
    }

  H = malloc(sizeof(struct HashTbl));
  if(H == NULL)
    FatalError("未分配空间");
  H->TableSize = NextPrime(TableSize);
  H->TheLists = malloc(sizeof(List) * H->TableSize); //这个地方是sizeof(List)而不是sizeof(struct ListNode)，因为这个地方是在给指针分配空间，给ListNode分配空间是在for循环中;
  if(H->TheLists == NULL)
    FatalError("未分配空间");

  for(i = 0;i < H->TableSize;i++)
    {
      H->TheLists + i = malloc(sizeof(struct ListNode));//每一次循环都调用malloc会使得效率变低，可以在循环之前通过只调用一次H->TheLists = malloc(sizeof(struct ListNode) * H->TableSize)来增加效率
      if(H->TheLists + i == NULL)
	FatalError("未分配空间");
      else
	(H->TheLists + i)->Next = NULL;
    }
  return H;
}

Position Find( ElementType Key, HashTable H )
{
  List L;
  Position P;
  L = H->TheLists + Hash(Key, H->TableSize);
  P = L->Next;
  while(P != NULL && P->Element != Key)
      P = P->Next;
  return P;
}

void Insert( ElementType Key, HashTable H )
{
  List L;
  Position P;
  L = H->TheLists + Hash(Key, H->TableSize);
  P = L->Next;
  while(P != NULL && P->Element != Key)
    P = P->Next;
  if(P == NULL)
    {
      P = malloc(sizeof(struct ListNode));
      if(P == NULL)
	FatalError("未分配空间");
      P->Element = Key;
      P->Next = L->Next;
      L->Next = P;
    }
}
