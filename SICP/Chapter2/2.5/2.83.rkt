#lang planet neil/sicp
(define number-type-list
  '(scheme-number rational real complex))
(put-coercion 'scheme-number 'rational
              (lambda (x) (make-rational x 1)))
(put-coercion 'rational 'real
              (lambda (x) (/ (* 1.0 (numer x))
                             (denom x))))
(put-coercion 'real 'complex
              (lambda (x) (make-complex-from-real-imag x 0)))
(define (raise x)
  (define (iter type-list)
    (if (< (length type-list) 2)
        (error "")
        (let ((type-x (type-tag x))
              (first-type (car type-list))
              (next-type (cadr type-list)))
          (if (eq? type-x first-type)
              ((get-coercion type-x next-type) x)
              (iter (cdr type-list))))))
  (iter number-type-list))
