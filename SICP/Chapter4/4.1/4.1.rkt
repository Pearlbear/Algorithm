#lang planet neil/sicp
;left-to-right
(define (list-of-values exps env)
  (if (no-operands? exps)
      '()
      (let ((first (eval (first-operand exps) env))
            (rest (list-of-values (rest-operand exps) env)))
        (cons first second))))
;right-to-left
(define (list-of-values exps env)
  (if (no-operands? exps)
      '()
      (let ((rest (list-of-values (rest-operand exps) env))
            (first (eval (first-operand exps) env)))
        (cons first second))))