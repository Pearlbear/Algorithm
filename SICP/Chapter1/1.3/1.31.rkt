#lang planet neil/sicp
(define square
  (lambda (x) (* x x)))
(define (even? x)
  (= (remainder x 2) 0))
(define (product term a next b)
  (if (> a b)
      1
      (* (term a) (product term (next a) next b))))
(define (product-iter term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (* result (term a)))))
  (iter a 1))

(define (factorial n)
  (product-iter (lambda (x) x) 1 (lambda (x) (+ x 1)) n))

(factorial 6)

(define (quart-pi)
  (product-iter (lambda (x) (if (even? x)
                           (/ (+ x 2) (+ x 1.0))
                           (/ (+ x 1) (+ x 2))))
           1
           (lambda (x) (+ x 1))
           100))

(quart-pi)