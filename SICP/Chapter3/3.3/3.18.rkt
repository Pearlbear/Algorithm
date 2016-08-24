#lang planet neil/sicp
(define (loop-list? list)
  (define (iter search visited)
    (cond ((not (pair? search)) #f)
          ((memq search visited) #t)
          (else (or (iter (car search) (cons search visited))
                    (iter (cdr search) (cons search visited))))))
  (iter list '()))
;没做出来,这个是看的答案,非常优美