#lang planet neil/sicp
(define (ln2-summands n)
    (cons-stream (/ 1.0 n)
		 (stream-map - (ln2-summands (+ 1 n)))))
(define ln2-stream
  (partial-sums (ln2-summands 1)))
(define ln2-accelerate-stream (euler-transform ln2-stream))
(define ln2-tableau-accelerate-stream
  (accelerated-sequence euler-transform ln2-stream))
