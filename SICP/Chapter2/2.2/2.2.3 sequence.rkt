#lang planet neil/sicp
(define (square x)
  (* x x))
(define (fib n)
  (define (try x y count)
    (if (= count 0)
        y
        (try (+ x y) x (- count 1))))
  (try 1 0 n))
(define (sum-odd-squares tree)
  (cond ((null? tree) nil)
        ((pair? tree)
         (+ (sum-odd-squares (car tree))
            (sum-odd-squares (cdr tree))))
        ((odd? tree) (square tree))
        (else 0)))

(define (even-fibs n)
  (define (next k)
    (if (> k n)
        nil
        (let ((f (fib k)))
          (if (even? f)
              (cons f (next (+ k 1)))
              (next (+ k 1))))))
  (next 0))

(define (filter predicate sequence)
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
(define (enumerate-interval low high)
  (if (> low high)
      nil
      (cons low (enumerate-interval (+ low 1) high))))
(define (enumerate-tree tree)
  (cond ((null? tree) nil)
        ((pair? tree)
         (append (enumerate-tree (car tree))
                 (enumerate-tree (cdr tree))))
        (else (list tree))))
(define (sum-odd-squares tree)
  (accumulate + 0
              (map square
                   (filter odd?
                           (enumerate-tree tree)))))
(define (even-fibs n)
  (accumulate cons nil
              (filter even?
                      (map fib
                           (enumerate-interval 0 n)))))
(define (list-fib-squares n)
  (accumulate cons nil
              (map square
                   (map fib
                        (enumerate-interval 0 n)))))
(define (product-of-squares-of-odd-elements sequence)
  (accumulate * 1
              (map square
                   (filter odd? sequence))))
(define (programer records)
  (accumulate max 0
              (map salary
                   (filter programmer? records))))