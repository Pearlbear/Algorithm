#lang planet neil/sicp
(define (make-accumulator sum)
  (lambda (x)
    (begin (set! sum (+ x sum))
           sum)))

(define A (make-accumulator 5))
(A 10)
(A 10)