#lang planet neil/sicp
(define (last-pair items)
  (let ((rest (cdr items)))
    (if (null? rest)
        items
        (last-pair rest))))
(last-pair (list 23 72 149 34))