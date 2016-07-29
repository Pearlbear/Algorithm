#lang planet neil/sicp
(define (double f)
  (lambda (x) (f (f x))))
(define (inc x)
  (+ x 1))
((double inc) 2)

(((double (double double)) inc) 5)
#|
(((double (lambda (x) (double (double x)))) inc) 5)
((double (double (double (double inc)))) 5)
((double (double (double (lambda (x) (inc (inc x)))))) 5)
((double (double (lambda (x) (inc (inc (inc (inc x)+))))) 5)
|#