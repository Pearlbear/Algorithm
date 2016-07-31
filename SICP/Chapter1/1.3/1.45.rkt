#lang planet neil/sicp
(define square
  (lambda (x) (* x x)))
(define average
  (lambda (x y) (/ (+ x y) 2)))
(define (exp x n)
  (if (= n 0)
      1
      (* x (exp x (- n 1)))))

(define (fixed-point f guess)
  (define (close-enough? x y)
    (let ((tolerance 0.00001))
      (< (abs (- x y)) tolerance)))
  (let ((f-value (f guess)))
    (display f-value)
    (display ":")
    (display guess)
    (newline)
    (if (close-enough? f-value guess)
        guess
        (fixed-point f f-value))))

(define (average-damp f)
  (lambda (x) (average (f x) x)))

(define (repeated f n)
  (define (compose f g)
    (lambda (x) (f (g x))))
  (if (= n 1)
      f
      (compose f (repeated f (- n 1)))))
;This is incorrect
(define (root x n)
  (fixed-point (repeated (average-damp (lambda (y) (/ x (exp y (- n 1)))))
                         (- n 2))
               1.0))
(root 32 5)