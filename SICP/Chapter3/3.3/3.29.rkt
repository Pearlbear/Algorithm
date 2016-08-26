#lang racket
(define (or-gate a1 a2 output)
  (inverter (and-gate (inverter a1 (make-wire))
                      (inverter a2 (make-wire))
                      (make-wire))
            output))
;or-gate-delay = 3 * inverter-delay + and-gate-delay