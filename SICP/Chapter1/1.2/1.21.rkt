#lang planet neil/sicp
(define square
  (lambda (x) (* x x)))
(define (smallest-divisor n)
    (define (find-divisor dividend divisor)
      (cond ((< dividend (square divisor)) dividend)
            ((= 0 (remainder dividend divisor)) divisor)
            (else (find-divisor dividend (+ divisor 1)))))
    (find-divisor n 2))
(smallest-divisor 199)
(smallest-divisor 1999)
(smallest-divisor 19999)