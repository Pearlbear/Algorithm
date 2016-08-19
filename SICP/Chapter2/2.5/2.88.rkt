#lang racket
(define (negative L)
  (if (empty-termlist? L)
      '()
      (let ((t (first-term L)))
        (adjoin-term (make-term (order t)
                                (negative (coeff t)))
                     (negative (rest-terms L))))))
(define (sub-terms L1 L2)
  (add-terms L1 (negative L2)))

(put 'sub '(polynomial polynomial)
     (lambda (p1 p2) (tag (sub-terms p1 p2))))
(put 'negative 'polynomial
     (lambda (p) (tag (make-poly (variable p)
                                 (negative (term-list p))))))