#lang planet neil/sicp
(define (install-poly-package)
  (define (=zero? x)
    (empty-termlist? (term-list x)))
  (put '=zero? '(polynomial)
       =zero?)
  'done)