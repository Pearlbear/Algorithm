#lang planet neil/sicp
(define (ordered-triples-sum n s)
  (filter (lambda (items) (= s (accumulate + 0 items)))
          (flatmap (lambda (i)
                     (flatmap (lambda (j)
                                (map (lambda (k) (list i j k))
                                     (enumerate-interval 1 (- j 1))))
                              (enumerate-interval 1 (- i 1))))
                   (enumerate-interval 1 n))))