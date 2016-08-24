#lang planet neil/sicp
(define (count-pairs x)
  (if (not (pair? x))
      0
      (+ (count-pairs (car x))
         (count-pairs (cdr x))
         1)))
;4
(define third (cons 'a '()))
(define second (cons 'b third))
(define first (cons second third))
(count-pairs first)
;7
(define third (cons 'a 'b))
(define second (cons third third))
(define first (cons second second))
(count-pairs first)
;never return
;制造一个循环的序对即可