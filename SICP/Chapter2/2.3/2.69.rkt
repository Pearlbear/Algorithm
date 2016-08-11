#lang planet neil/sicp
(define (successive-merge leaf-set)
  (define (iter result rest-set)
    (if (null? rest-set)
        result
        (iter (make-code-tree
               (car rest-set) result)
              (cdr rest-set))))
  (iter (car leaf-set) (cdr leaf-set)))