#lang planet neil/sicp
#|
因为递归的调用(sqrt-stream x)会不断产生新的数列,会重复计算
如果不使用memo-proc的优化,那么效果和上面是一样的
|#
