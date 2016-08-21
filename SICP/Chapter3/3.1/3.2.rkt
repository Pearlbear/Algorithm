#lang planet neil/sicp
(define (make-monitored f)
  (let ((times 0))
    (lambda (x)
      (cond ((eq? x 'how-many-calls?)
             (display times))
            ((eq? x 'reset-count)
             (set! times 0))
            (else (begin (set! times (+ times 1))
                         (f x)))))))

(define s (make-monitored sqrt))
(s 100)
(s 'how-many-calls?)