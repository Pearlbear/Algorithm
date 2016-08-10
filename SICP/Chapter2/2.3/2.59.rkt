#lang planet neil/sicp
(define (union-set set1 set2)
  (cond ((null? set1) set2)
        ((null? set2) set1)
        (else (union-set (cdr set1)
                         (if (element-of-set? (car set1) set2)
                             set2
                             (cons (car set1) set2))))))