#lang planet neil/sicp
(define (square x)
  (* x x))
(define (compose f g)
  (lambda (x) (f (g x))))
#|
(define (repeated f n)
  (lambda (x)
    (define (iter g n)
      (if (= n 0)
          x
          (g (iter g (- n 1)))))
    (iter f n)))
|#
;Better solution. Very elegant! 
(define (repeated f n)
  (if (= n 1)
      f
      (compose f (repeated f (- n 1)))))
((repeated square 2) 5)