#lang planet neil/sicp
;用了(n-2)次加法
;如果没有使用memo-proc的话,每一次第n个数都会计算第(n-2)和第(n-1)个数,递归下去就是指数级增长的
