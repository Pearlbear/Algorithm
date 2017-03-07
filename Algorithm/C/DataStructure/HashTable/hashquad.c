enum KindOfEntry
  {
    Legitimate,
    Empty,
    Deleted
  };

struct HashEntry
{
  ElementType Element;
  enum KindOfEntry Info;
};

typedef struct HashEntry Cell;
//hashsep里面的TheLists是指针的指针，为什么这里的TheCells不是？
//难道是想把数组和HashTbl放到一起？
struct HashTbl
{
  int TableSize;
  Cell *TheCells;
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
  H->TheCells = malloc(sizeof(Cell) * H->TableSize);
  if(H->TheCells == NULL)
    FatalError("未分配空间");
  for(i = 0;i < H->TableSize;i++)
    {
      (H->TheCells + i)->Info = Empty;
    }
  return H;
}

Position Find( ElementType Key, HashTable H )
{
  /*
    这个例程不行，因为若没有找到，最后应该返回的是空位置以待插入
  Position P;
  int i;
  for(i = 0;i*i + Hash(Key, H->TableSize) < H->TableSize;i++)
    {
      P = H->TheCells + Hash(Key, H->TableSize) + i*i;
      if(P->Element == Key && P->Info == Legitimate)
	return P;
    }
  return NULL;
  */
  Position P;
  int i;
  P = Hash(Key, H->TableSize);
  i = 0;
  while(((H->TheCells + P)->Info != Empty) && ((H->TheCells + P)->Element != Key))
    {
      P += (i<<1) -1;//用前项表示的平方函数
      if(P >= H->TableSize)
	P -= H->TableSize;
    }
  return P;
}

void Insert( ElementType Key, HashTable H )
{
  Position P;
  P = Find(Key, H);
  if((H->TheCells + P)->Info != Legitimate)
    {
      (H->TheCells + P)->Info = Legitimate;
      (H->TheCells + P)->Element = Key;
    }
}

/*
  再散列
 */
HashTable ReHash(HashTable H)
{
  HashTable NewTable;
  int i;
  NewTable = InitializeTable(H->TableSize << 1);
  for(i = 0;i < H->TableSize;i++)
    {
      if((H->TheCells+i)->Info == Legitimate)
	  Insert((H->TheCells+i)->Element, NewTable);
    }
  DestroyTable(H);
  return NewTable;
}
