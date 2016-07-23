#lang planet neil/sicp
(define (square x)
  (* x x))
(define (even? x)
  (= (remainder x 2) 0))
;recursion
(define (exponent-r a n)
  (if (= n 0)
      1
      (* a (exponent-r a (- n 1)))))
;iteration
(define (exponent-i a n)
  (define (exponent-iter count product)
    (if (= count 0)
        product
        (exponent-iter (- count 1) (* a product))))
  (exponent-iter n 1))
;O(log(n))
(define (exponent-square a n)
    (cond ((= n 0) 1)
          ((even? n) (square (exponent-square a (/ n 2))))
          (else (* a (exponent-square a (- n 1))))))
(exponent-square 5 1000)