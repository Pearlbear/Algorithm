#lang racket
;原因在于每一次迭代多了k次queen-cols过程计算，相当于多了k^k指数级的queen-cols