#lang planet neil/sicp
(define (reverse items)
  (let ((rest (cdr items)))
    (if (null? rest)
        items
        (append (reverse rest) (list (car items))))))
;思考有点儿困难
(define (deep-reverse items)
  (if (pair? items)
      (append (deep-reverse (cdr items)) (list (deep-reverse (car items))))
      items))
(deep-reverse (list (list 1 2) (list 3 4)))