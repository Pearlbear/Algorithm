#lang planet neil/sicp
(define (+ a b)
  (if (= a 0)
      b
      (inc (+ (dec a) b))))
#|
(+ 5 8)
(inc (+ 4 8))
(inc (inc (+ 3 8)))
(inc (inc (inc (+ 2 8))))
(inc (inc (inc (inc (+ 1 8)))))
(inc (inc (inc (inc (inc (+ 0 8))))))
(inc (inc (inc (inc (inc 8)))))
(inc (inc (inc (inc 9))))
(inc (inc (inc 10)))
(inc (inc 11))
(inc 12)
13
|#
(define (+ a b)
  (if (= a 0)
      b
      (+ (dec a) (inc b))))
#|
(+ 5 8)
(+ 4 9)
(+ 3 10)
(+ 2 11)
(+ 1 12)
(+ 0 13)
13
|#