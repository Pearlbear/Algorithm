#lang planet neil/sicp
(define (X s)
  (define x
    (cons-stream 1 (mul-series (scale-stream (stream-cdr s) -1)
			       s)))
  x)
