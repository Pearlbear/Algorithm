#lang planet neil/sicp
(define tolerance 0.00001)
(define square
  (lambda (x) (* x x)))
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

(define (deriv g)
  (let ((dx 0.00001))
    (lambda (x)
      (/ (- (g (+ x dx)) (g x))
         dx))))
(define (newton-transform g)
  (lambda (x) (- x (/ (g x) ((deriv g) x)))))
(define (fixed-point-of-transform g transform guess)
  (fixed-point (transform g) guess))
(define (sqrt x)
  (fixed-point-of-transform (lambda (y) (- (square y) x))
                             newton-transform
                             1.0))
(sqrt 2)