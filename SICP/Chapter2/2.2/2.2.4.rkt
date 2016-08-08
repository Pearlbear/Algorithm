#lang planet neil/sicp
;beside below flip-vert flip-horiz
(define (flipped-pairs painter)
  (let ((pair (beside painter (flip-vert painter))))
    (beside pair pair)))
(define (right-split painter n)
  (if (= n 0)
      painter
      (let ((smaller (right-split painter (- n 1))))
        (beside painter (below smaller smaller)))))
(define (corner-split painter n)
  (if (= n 0)
      painter
      (let ((right (right-split painter (- n 1)))
            (up (up-split painter (- n 1)))
        (beside (below painter (beside up up))
                (below (below right right) (corner-split painter n)))))))
(define (square-limit painter n)
  (let ((quarter (corner-split painter n)))
    (let ((half (beside (flip-horiz sqarter) sqarter)))
      (below (flip-vert half) half))))