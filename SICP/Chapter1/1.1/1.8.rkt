#lang planet neil/sicp

(define square
  (lambda (x) (* x x)))
(define cube
  (lambda (x) (* x x x)))
(define abs
  (lambda (x) (if (< x 0) (- x) x)))
(define average
  (lambda (x y) (/ (+ x y) 2)))
(define good-enough？
  (lambda (x guess diff) (< (abs (- x (cube guess))) diff)))
(define improve
  (lambda (x guess) (/ (+ (/ x (* guess guess)) (* 2 guess)) 3)))
(define cube-root-iter
  (lambda (x guess diff)
    (cond ((good-enough？ x guess diff) guess)
        (else (cube-root-iter x (improve x guess) diff)))))

(define cube-root
  (lambda (x) (cube-root-iter x 1.0 0.0001)))

(cube-root 27)