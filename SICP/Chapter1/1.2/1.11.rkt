#lang planet neil/sicp
;recursive
(define (f-r n)
  (if (< n 3)
      n
      (+ (f-r (- n 1)) (* 2 (f-r (- n 2))) (* 3 (f-r (- n 3))))))
(f-r 6)
#|
f(n) = f(n-1) + 2f(n-2) + 3f(n-3)
f(0) = 0, f(1) = 1, f(2) = 2
f(3) = f(2) + 2f(1) + 3f(0)
|#
;iteration
(define (f-i n)
  (define (f-iter count a b c)
    (if (= count 0)
        c
        (f-iter (- count 1) (+ a (* 2 b) (* 3 c)) a b)))
  (f-iter n 2 1 0))
(f-i 6)
        