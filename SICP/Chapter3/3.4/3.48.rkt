#lang racket
;因为如果a1账户较小的话,那么都会先获取进入a1账户的锁,就不会在未拿到a1锁的情况下去拿a2的锁,这样谁先拿到a1锁就肯定可以拿到a2的锁
(define (make-account account number)
  (define (withdraw...))
  (define (dispatch m)
    (cond ((eq? m 'number) number)
          ...))
  dispatch)
(define (serialized-exchange account1 account2)
  (let ((number1 (account1 'number))
        (number2 (account2 'number))
        (serializer1 (account1 'serializer))
        (serializer2 (account2 'serializer)))
    (if (< number1 number2)
        ((serializer1 (serializer2 exchange))
         account1
         account2)
        ((serializer2 (serializer1 exchange))
         account2
         account1))))