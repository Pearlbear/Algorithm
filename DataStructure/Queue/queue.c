#define MinQueueSize (5)

struct QueueRecord
{
  int Capacity;
  int Size;
  int Front;
  int Rear;
  ElementType *Array;
};

int IsEmpty( Queue Q )
{
  return Q->Size == 0;
}

void MakeEmpty( Queue Q )
{
  Q->Front = 1;
  Q->Rear = 0;
  Q->Size = 0;
}

void Enqueue( ElementType X, Queue Q )
{
  if(IsFull(Q))
    Error("队列已满");
  else
    {
      Q->Rear = Succ(Q->Rear, Q);
      Q->Array[Q->Rear] = X;
      Q->Size++;
    }
  
}

/*
  很巧妙的例程，if里面的条件判断式既可判断又可对Value+1，提高了效率
 */
static int Succ(int Value, Queue Q)
{
  if(++Value == Q->Capacity)
    Value = 0;
  return Value;
}
