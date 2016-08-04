#lang planet neil/sicp
(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
        result
        (iter (op result (car rest))
              (cdr rest))))
  (iter initial sequence))
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
;1/6 3/2
(fold-left list nil (list 1 2 3))
(accumulate list nil (list 1 2 3))
;op需满足:op参数交换位置后与原来的op一样