#lang planet neil/sicp
#|
(define (make-rat n d)
  (let ((g (gcd n d)))
    (if (and (< d 0) (< n 0))
        (cons (/ (- n) g) (/ (- d) g))
        (cons (/ n g) (/ d g)))))
|#
;More elegant.
(define (make-rat n d)
  (let ((g ((if (< d 0) - +) (abs (gcd n d)))))
        (cons (/ n g) (/ d g))))