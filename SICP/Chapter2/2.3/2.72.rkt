#lang racket
#|
最频繁的符号只用迭代一次，因此是O(1)
最不频繁的符号会迭代树的深度次，即(n-1)次，element-of-set会迭代O(n)次，因此是O(n^2)
|#