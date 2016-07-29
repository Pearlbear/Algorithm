#lang planet neil/sicp
(define (compose f g)
  (lambda (x) (f (g x))))
(define (repeated f n)
  (if (= n 1)
      f
      (compose f (repeated f (- n 1)))))
(define (smooth f)
  (let ((dx 0.0001))
    (lambda (x) (/ (+ (f (- x dx))
                      (f x)
                      (f (+ x dx)))
                   3))))
;This is incorrect.
(define (repeated-smooth f n)
  (repeated (smooth f) n))
;This is correct.有点儿不好理解
(define (repeated-smooth f n)
  ((repeated smooth n) f))