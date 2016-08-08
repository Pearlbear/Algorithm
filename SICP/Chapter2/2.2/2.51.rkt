#lang planet neil/sicp
(define (below painter1 painter2)
  (let ((split-point (make-vect 0 0.5)))
    (let ((paint-top
           (transform-painter painter2
                              split-point
                              (make-vect 1 0.5)
                              (make-vect 0 1)))
          (paint-bottom
           (transform-painter painter1
                              (make-vect 0 0)
                              (make-vect 1 0)
                              split-point)))
      (lambda (frame)
        (paint-bottom frame)
        (paint-top frame)))))

(define (below painter1 painter2)
  (anti-clockwise-90 (beside (clockwise-90 painter1) (clockwise-90 painter2))))