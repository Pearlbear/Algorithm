#lang planet neil/sicp
(define (partial-sums stream)
  (cons-stream (stream-car stream)
	       (add-streams (partial-sums stream) (stream-cdr stream))))
;So elegant
(define (partial-sums stream)
  (add-streams stream (cons-stream 0 (partial-sums stream))))
