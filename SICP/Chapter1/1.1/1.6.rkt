#lang planet neil/sicp
#|
用new-if来执行会出现内存耗尽的情况，原因在于：
解释器使用的是应用序求值，在使用new-if时会把所有参数求值后再应用，因此第三个参数就会不停去递归，最终耗尽内存；
if语句比较特殊，会先求值predicate，再根据predicate的值决定求值then-clause还是else-clause，因此不会求值所有参数。
|#
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

(define (abs x)
  (if (< x 0) (- x) x))
(define (average x y) (/ (+ x y) 2))
(define (good-enough? x guess diff) (< (abs (- (/ x guess) guess)) diff))
(define (improve x guess) (average (/ x guess) guess))
(define (square-root-iter x guess diff)
  (new-if (good-enough? x guess diff)
      guess
      (square-root-iter x (improve x guess) diff)))
(define (square-root x) (square-root-iter x 1.0 0.0001))
(square-root 2)

