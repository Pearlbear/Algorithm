#lang planet neil/sicp
(define (triples s t u)
  (cons-stream (list (stream-car s) (stream-car t) (stream-car u))
               (interleave (triples (stream-cdr s) (stream-cdr t) (stream-cdr u))
                           (stream-map (lambda (x) (cons-stream (stream-car s) x))
                                       (stream-cdr (pairs t u))))))
(define phythagorean-numbers
  (define (equal-square-sum? i j k)
    (= (+ (square i) (square j)) (square k)))
  (stream-filter (lambda (triple) (equal-square-sum? (stream-car triple)
                                                     (stream-cadr triple)
                                                     (stream-caddr triple)))
                 (triples integers integers integers)))