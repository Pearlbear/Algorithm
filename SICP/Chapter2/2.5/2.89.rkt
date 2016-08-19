#lang racket
(define (first-term term-list)
  (list (- (length term-list) 1) (car term-list)))
(define (adjoin-term term term-list)
  (if (=zero? (coeff term))
      term-list
      (cons (coeff term) term-list)))