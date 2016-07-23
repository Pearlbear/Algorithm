#lang planet neil/sicp
(define (double x)
  (+ x x))
(define (even? x)
  (= (remainder x 2) 0))
(define (halve x)
  (/ x 2))

(define (multiply a b)
  (define (multiply-iter count b sum)
    (cond ((= count 0) sum)
          ((even? count) (multiply-iter (halve count) (double b) sum))
          (else (multiply-iter (- count 1) b (+ sum b)))))
  (multiply-iter a b 0))

(multiply 7 3)