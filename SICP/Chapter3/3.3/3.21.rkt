#lang racket
;其实队列已经空了,只是因为在delete-queue的实现中没有清除最后一个指针而已,所以解释器把它显示出来了
(define (print-queue queue)
  (display "(")
  (define (iter current-item)
    (if (pair? current-item)
        (begin (display "-- " (car current-item))
               (iter (cdr current-item)))
        (display ")")))
  (iter (car queue)))
