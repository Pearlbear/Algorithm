#lang planet neil/sicp
;将good-enough，improve等变为内部定义
(define (abs x)
  (if (< x 0) (- x) x))
(define (average x y)
  (/ (+ x y) 2))

(define (square-root x)
  (define diff 0.001)
  (define (good-enough? guess)
    (< (abs (- (/ x guess) guess)) diff))
  (define (improve guess)
    (average (/ x guess) guess))
  (define (square-root-iter guess)
    (cond ((good-enough? guess) guess)
          (else (square-root-iter (improve guess)))))
  (square-root-iter 1.0))

(square-root 2)