#lang planet neil/sicp
(define (reverse items)
  (let ((rest (cdr items)))
    (if (null? rest)
        items
        (append (reverse rest) (list (car items))))))
(list 1 4 9 16 25 36)
(reverse (list 1 4 9 16 25 36))
