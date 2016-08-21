#lang planet neil/sicp
(define (withdraw amount)
  (let ((balance 100))
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds")))
(withdraw 20)
(withdraw 30)