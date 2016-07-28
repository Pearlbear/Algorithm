#lang planet neil/sicp
(define tolerance 0.00001)
(define average
  (lambda (x y) (/ (+ x y) 2)))
(define (close-enough? x y)
  (< (abs (- x y)) tolerance))
(define (fixed-point f guess)
  (let ((f-value (f guess)))
    (if (close-enough? f-value guess)
        guess
        (fixed-point f f-value))))
(fixed-point cos 1.0)
(define (sqrt x)
  (fixed-point (lambda (y) (average y (/ x y)))
               1.0))
(sqrt 2)