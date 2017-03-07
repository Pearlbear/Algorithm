#ifndef _BinHeap_H
#define _BinHeap_H

#define MaxTrees (14)
#define Capacity (16383)

struct BinNode;
typedef struct BinNode *BinTree;
struct Collection;
typedef struct Collection *BinQueue;

BinQueue Initialize( void );
BinTree CombineTrees(BinTree T1, BinTree T2);
BinQueue Merge(BinQueue H1, BinQueue H2);
ElementType DeleteMin(BinQueue H);

#endif
