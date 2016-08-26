#lang racket
(define (ripple-carry-adder a b s c)
  (define (iter rest-a rest-b rest-s c-in)
    ((iter (cdr rest-a) (cdr rest-b) (cdr rest-s) c-in)
     (full-adder (car rest-a) (car rest-b) c-in (car rest-s) c)))
  (iter a b s 0))
;ripple-delay = n * full-adder-delay
;             = n * (2 * half-adder-delay + or-gate-delay)
;             = n * (2 * (and-gate-delay + max(or-gate-delay, (and-gate-delay + inverter-delay))) + or-gate-delay)