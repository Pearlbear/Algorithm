#lang racket
(define (install-polynomial-package) 
  (define (first-term-dense term-list)
    (list (- (length term-list) 1) (car term-list)))
  (define (adjoin-term-dense term term-list)
    (if (=zero? (coeff term))
        term-list
        (cons (coeff term) term-list)))

  (define (first-term-sparse term-list)
    (car term-list))
  (define (adjoin-term-sparse term term-list)
    (if (=zero? (coeff term))
        term-list
        (cons term term-list)))
  
  (put 'first-term 'dense first-term-dense)
  (put 'adjoin-term 'dense adjoin-term-dense)
  (put 'first-term 'sparse first-term-sparse)
  (put 'adjoin-term 'sparse adjoin-term-sparse))s