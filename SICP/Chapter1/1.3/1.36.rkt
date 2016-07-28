#lang planet neil/sicp
(define tolerance 0.00001)
(define average
  (lambda (x y) (/ (+ x y) 2)))
(define (close-enough? x y)
  (< (abs (- x y)) tolerance))
(define (fixed-point f guess)
  (let ((f-value (f guess)))
    (display f-value)
    (display ":")
    (display guess)
    (newline)
    (if (close-enough? f-value guess)
        guess
        (fixed-point f f-value))))
(fixed-point (lambda (x) (/ (log 1000) (log x))) 2.0)
(display "----")
(newline)
(fixed-point (lambda (x) (average x (/ (log 1000) (log x)))) 2.0)