#lang planet neil/sicp
(define (stream-limit stream tolerance)
  (define (iter current-stream previous)
    (let ((current (stream-car current-stream)))
      (if (< (abs (- current previous))
	     tolerance)
	  current
	  (iter (stream-cdr current-stream) current))))
  (iter (stream-cdr stream) (stream-car stream)))
;或者直接递归
(define (stream-limit stream tolerance)
  (let ((first (stream-car stream))
	(second (stream-car (stream-cdr stream))))
    (if (< (abs (- first second))
	   tolerance)
	first
	(stream-limit (stream-cdr stream) tolerance))))
