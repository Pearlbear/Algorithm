#lang planet neil/sicp
(define number-type-list
  '(scheme-number rational real complex))
(define (drop x)
  (if (can-drop? x)
      (drop (project x))
      x))
(define (can-drop? x)
    (eq? (raise (project x)) x))
(define (project x)
  (let ((type (type-tag x)))
    (if (eq? type (car number-type-list))
        (- x 1);返回一个不等于x的数,表示project失败
        ((define (iter type-list last-type)
          (let ((current-type (car type-list)))
            (if (eq? type current-type)
                ((get-project current-type last-type) x)
                (iter (cdr type-list) current-type))))
         (iter (cdr number-type-list) (car number-type-list))))))
(put-project 'rational 'scheme-number
             (lambda (x) (/ (* 1.0 (numer x))
                            (denom x))))
(put-project 'real 'rational
             (lambda (x) (make-rational x 1)))
(put-project 'complex 'real
             (lambda (x) (real x)))