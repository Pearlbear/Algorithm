#lang planet neil/sicp
(define (double x)
  (+ x x))
(define (even? x)
  (= (remainder x 2) 0))
(define (halve x)
  (/ x 2))

(define (multiply a b)
  (cond ((= a 0) 0)
        ((even? a) (double (multiply (halve a) b)))
        (else (+ b (multiply (- a 1) b)))))
(multiply 23 2)