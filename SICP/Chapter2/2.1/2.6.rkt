#lang planet neil/sicp
(define zero
  (lambda (f) (lambda (x) x)))
(define (add-1 n)
  (lambda (f) (lambda (x) (f ((n f) x)))))
(define one
  (lambda (f) (lambda (x) (f x))))  ;(add-1 zero)
(define two
  (lambda (f) (lambda (x) (f (f x)))))
;答案可以验证是正确的，比如(add one two)，但是不知道怎么推出来
(define (add a b)
  (lambda (f) (lambda (x) ((a f) ((b f) x)))))