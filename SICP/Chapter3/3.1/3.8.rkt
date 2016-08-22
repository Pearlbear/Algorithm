#lang planet neil/sicp
(define f
  (let ((a 0))
    (lambda (x)
      (begin (display x)
             (if (= x 0)
                 (begin (set! a 1)
                        a)
                 (- a))))))
  
(+ (f 0) (f 1))