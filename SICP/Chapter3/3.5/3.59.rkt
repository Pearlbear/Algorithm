#lang planet neil/sicp
;a)
(define (integrate-series stream)
  (mul-streams stream (stream-map / ones integers)))
;b)
(define cosine-series
  (cons-stream 1
	       (integrate-series (scale-stream sine-series -1))))
(define sine-series
  (cons-stream 0
	       (integrate-series cosine-series)))
