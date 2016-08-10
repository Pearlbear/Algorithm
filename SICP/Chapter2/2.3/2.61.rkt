#lang planet neil/sicp
(define (adjoin-set x set)
  (cond ((null? set) (cons x '()))
        ((= x (car set)) set)
        ((< x (car set)) (cons x set))
        (else (cons (car set) (adjoin-set x (cdr set))))))
;未排序时adjoin-set会遍历整个set,是⦶(n)的增长速度,排序后平均是⦶(n/2)的增长速度