#lang planet neil/sicp
#|
当对很小的数开方时，误差会很大，比如对0.0001开方，结果是0.03，而不是0.01；
当对很大的数开方时，会陷入无限循环，比如对10000000000000开方是无限循环，因为数的表
示位数有限，guess是3162277.6601683795时，平方后是10000000000000.002，永远不可能与
10000000000000相差少于0.001，就无限循环了，不过，少一个0就可以求出正确答案。

|#
(define square
  (lambda (x) (* x x)))
(define (abs x)
  (if (< x 0) (- x) x))
(define (average x y)
  (/ (+ x y) 2))
(define (improve x guess)
  (average (/ x guess) guess))
(define (good-enough? x guess diff)
  (< (abs (- (square guess) x)) diff))
;(define (good-enough? x guess diff)
;  (< (abs (- (improve x guess) guess));改进方式，不好的一点是：improve被调用了两次
;     (* diff guess)))
(define (square-root-iter x guess diff)
  (if (good-enough? x guess diff)
       guess
       (square-root-iter x (improve x guess) diff)))
(define (square-root x) (square-root-iter x 1.0 0.001))

(square-root 0.0001)
(square-root 10000000000000)