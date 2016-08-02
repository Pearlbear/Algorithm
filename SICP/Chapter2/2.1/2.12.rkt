#lang planet neil/sicp
(define (make-center-percent center percent)
  (make-center-width center (* center percent)))
(define (percent i)
  (/ (width i) (center i)))