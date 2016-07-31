#lang planet neil/sicp
(define (iterative-improve good-enough? improve)
  (lambda (guess x) (if (good-enough? guess x)
                        guess
                        ((iterative-improve good-enough? improve) (improve guess x) x))))

(define (square x)
  (* x x))
(define (average x y)
  (/ (+ x y) 2))
(define (sqrt-good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))
(define (sqrt-improve guess x)
  (average guess (/ x guess)))
(define (sqrt x)
  ((iterative-improve sqrt-good-enough? sqrt-improve) 1.0 x))
(sqrt 2)

;智商不够用