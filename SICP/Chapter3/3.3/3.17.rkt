#lang planet neil/sicp
(define (count-pairs x)
  (let ((checked-pairs '()))
    (define (iter x)
      (if (not (pair? x))
          0
          (+ (iter (car x))
             (iter (cdr x))
             (if (element-of-set? x checked-pairs)
                 0
                 (begin (set! checked-pairs (adjoin-set x checked-pairs))
                        1))))))
  (iter x))