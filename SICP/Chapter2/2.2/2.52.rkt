#lang planet neil/sicp
;b)
(define (corner-split painter n)
  (if (= n 0)
      painter
      (beside (below painter (up-split painter (- n 1)))
              (below (right-split painter (- n 1)) (corner-split painter (- n 1))))))
;c)
(define (square-limit painter n)
  ((square-of-four flip-vert clockwise 180 identity flip-horiz)
   (corner-split painter n)))