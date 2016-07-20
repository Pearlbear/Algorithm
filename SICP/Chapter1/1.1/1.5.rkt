#lang planet neil/sicp
(define (p) (p))
(define (test x y)
  (if (= x 0)
      x
      y))
(test 0 (p))
;p被定义为自身，如果是应用序的话，代入(test 0 (p))时会对(p)求值，会出现无限循环；
;正则序在代入时不会求值，真正用到时才会求值，if永远不会用到(p)，因此不会无限循环。