#lang planet neil/sicp
(define (X s)
  (define x
    (cons-stream 1 (mul-series (scale-stream (stream-cdr s) -1)
			       s)))
  x)
;幂级数的除法是什么?
(define (div-series s1 s2)
  (mul-series s1 (X s2)))
(define tan-series
  (div-series sine-series cosine-series))
