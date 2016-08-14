#lang planet neil/sicp
;a)
(define (install-division1-package)
  (define file
    (list (list 'Jack 22000)
          (list 'Joe 11000)))
  (define (get-name record)
    (car record))
  (define (get-salary record)
    (cadr record))
  (define (get-record name)
    (define (iter name rest-data)
      (if (eq? name (get-name (car rest-data)))
          (car rest-data)
          (iter name (cdr rest-data))))
    (iter name file))
  (put 'get-record 'division1 get-record)
  (put 'get-salary 'division1 get-salary)
  'done)

(define (get-record name)
  (apply-generic 'get-record name))
;b)
(define (get-salary name)
  (get-salary (get-record name)))
;c)
;a中的get-record已经实现了,并且不应该传入表为参数,因为每个分支应该有自己的数据结构
;d)
;只需实现一个新的install-package,在自己的数据结构中提供get-record和get-salary,并将其put进操作表中即可