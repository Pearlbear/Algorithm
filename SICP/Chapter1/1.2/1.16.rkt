#lang planet neil/sicp
(define (square x)
  (* x x))
(define (even? x)
  (= (remainder x 2) 0))

(define (exponent-square-i a n)
  (define (exponent-iter b count power)
    (cond ((= count 0) power)
    ((even? count) (exponent-iter (square b) (/ count 2) power))
    (else (exponent-iter b (- count 1) (* b power)))))
  (exponent-iter a n 1))

(exponent-square-i 5 5)