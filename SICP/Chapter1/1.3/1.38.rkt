#lang planet neil/sicp
(define (cont-frac n d k)
  (define (try count)
    (if (= k count)
        (d k)
        (/ (n count) (+ (d count) (try (+ count 1))))))
  (try 1))
(define (e-euler i)
  (if (= (remainder i 3) 2)
      (/ (+ i 1) 1.5)
      1))
(+ 2.0 (cont-frac (lambda (x) 1)
           e-euler
           1000))