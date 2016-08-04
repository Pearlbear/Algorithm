#lang planet neil/sicp
(define (dot-product v w)
  (accumulate + 0 (map * v w)))
(define (matrix-*-vector m v)
  (map (lambda (m-row) (dot-product m-row v)) m))
(define (transpose mat)
  (accumulate-n cons nil mat))
(define (matrix-*matrix m n)
  (map (lambda (n-collum) (matrix-*-vector m n-collum)) (transpose n)))
