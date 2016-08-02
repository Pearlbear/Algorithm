#lang planet neil/sicp
(define (list-ref item n)
  (if (= n 0)
      (car item)
      (list-ref (cdr item) (- n 1))))

(define (length item)
  (if (null? item)
      0
      (+ 1 (length (cdr item)))))

(define (length item)
  (define (iter a count)
    (if (null? a)
        count
        (iter (cdr a) (+ 1 count))))
  (iter item 0))

(define (append list1 list2)
  (if (null? list1)
      list2
      (cons (car list1) (append (cdr list1) list2))))