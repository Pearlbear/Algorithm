#lang racket
#|
n=5
                    {a b c d e} 31
                     /           \
                {a b c d} 15      e 16
                 /     \
           {a b c} 7    d 8
             /    \
        {a b} 3    c 4
         /   \
      a 1    b 2
最少只用1个二进制位，最多用n-1个二进制位
|#