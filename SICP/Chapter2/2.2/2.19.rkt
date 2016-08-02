#lang planet neil/sicp
(define (first-denomination items)
  (car items))
(define (except-first-denomination items)
  (cdr items))
(define (no-more? items)
  (null? items))
;不会影响，因为递归过程会计算出所有的可能性，谁先谁后并不重要；但可能会影响计算的时间