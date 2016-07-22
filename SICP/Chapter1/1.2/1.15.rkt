#lang planet neil/sicp
(define (count x)
  (define (count-iter n times)
    (if (< n 0.1)
        times
        (count-iter (/ n 3) (+ times 1))))
  (count-iter x 0))
(count 12.15);a)计算次数
;b)不是尾递归，所以空间复杂度是O(log3(a));
;时间复杂度也是O(log3(a))