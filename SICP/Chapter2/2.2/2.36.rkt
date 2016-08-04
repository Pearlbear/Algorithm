#lang planet neil/sicp
(define (accumulate-n op init seqs)
  (define (iter proc seq)
    (if (null? seq)
        nil
        (cons (proc (car seq))
              (iter proc (cdr seq)))));实际上就是map操作
  (if (null? (car seqs))
      nil
      (cons (accumulate op init (iter car seqs))
            (accumulate-n op init (iter cdr seqs)))))
;还没建立起map的抽象层，没有第一时间想到map操作