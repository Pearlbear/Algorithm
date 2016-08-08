#lang planet neil/sicp
(define (make-vect x y)
  (cons x y))
(define (xcor-vect v)
  (car v))
(define (ycor-vect v)
  (cdr v))

(define (make-segment v-start v-end)
  (cons v-start v-end))
(define (start-segment segment)
  (car segment))
(define (end-segment segment)
  (cdr segment))