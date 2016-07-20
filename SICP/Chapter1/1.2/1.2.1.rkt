#lang planet neil/sicp
#|
(define (factorial n)
  (define (factorial-iter n product)
    (if (= n 1)
        product
        (factorial-iter (- n 1) (* n product))))
  (factorial-iter n 1))
|#
(define (factorial n)
  (define (factorial-iter present product)
    (if (> present n)
        product
        (factorial-iter (+ present 1) (* present product))))
  (factorial-iter 1 1))
(factorial 3)