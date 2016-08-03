#lang planet neil/sicp
(define (fringe tree)
  (if (null? tree)
      nil
      (let ((first (car tree)))
        (if (pair? first)
            (append (fringe first)
                    (fringe (cdr tree)))
            (cons first (fringe (cdr tree)))))))
(define my-tree (list 1 (list 2 (list 3 4) (list 5 6)) (list 7 (list 8))))
(fringe my-tree)