#lang planet neil/sicp

(define (abs x)
  (if (< x 0) (- x) x))
(define (average x y) (/ (+ x y) 2))
(define (good-enough？ x guess diff) (< (abs (- (/ x guess) guess)) diff))
(define (improve x guess) (average (/ x guess) guess))
(define (square-root-iter x guess diff)
  (cond ((good-enough？ x guess diff) guess)
        (else (square-root-iter x (improve x guess) diff))))

(define (square-root x) (square-root-iter x 1.0 0.0001))

(square-root 2)