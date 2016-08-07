#lang planet neil/sicp
(define (enumerate n)
  (accumulate append
              nil
              (map (lambda (i) (map (lambda (j) (list i j))
                                    (enumerate-interval 1 (- i 1))))
                   (enumerate-interval 1 n))))
(define (flatmap proc seq)
  (accumulate append nil (map proc seq)))
(define (prime-sum? pair)
  (prime? (+ (car pair) (car (cdr pair)))))
(define (make-pair-sum pair)
  (let ((i (car pair))
        (j (car (cdr pair))))
    (list i j (+ i j))))
(define (prime-sum-pairs n)
  (map make-pair-sum
       (filter prime-sum? (enumerate n))))