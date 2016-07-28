#lang planet neil/sicp
#|
黄金分割率公式：x^2 = x + 1
两边同除以x：   x = 1 + 1/x
|#
(define tolerance 0.00001)
(define (close-enough? x y)
  (< (abs (- x y)) tolerance))
(define (fixed-point f guess)
  (let ((f-value (f guess)))
    (if (close-enough? f-value guess)
        guess
        (fixed-point f f-value))))
(define golden
  (fixed-point (lambda (x) (+ 1 (/ 1 x))) 1.0))
golden