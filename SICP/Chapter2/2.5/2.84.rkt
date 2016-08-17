#lang planet neil/sicp
(define number-type-list
  '(scheme-number rational real complex))
(define (equal-args type-list . args)
  (let ((type-tags (map type-tag args)))
    (if (= (length args) 2)
        (let ((first-type (car type-list))
              (type1 (car type-tags))
              (type2 (cadr type-tags))
              (a1 (car args))
              (a2 (cadr args)))
          (if (eq? type1 type2)
              args
              (if (eq? type1 first-type)
                  (equal-args (cdr type-list)
                         (raise a1)
                         a2)
                  (equal-args (cdr type-list)
                         a1
                         (raise a2))))))))
(define (apply-generic op . args)
  (let ((type-tags (map type-tag args)))
    (let ((proc (get op type-tags)))
      (if proc
          (apply proc (map contents args))
          (apply-generic op (equal-args number-type-list args))))))