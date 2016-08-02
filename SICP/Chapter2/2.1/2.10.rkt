#lang planet neil/sicp
(define (div-interval x y) 
   (if (<= (* (lower-bound y) (upper-bound y)) 0) 
       (error "Division error (interval spans 0)" y) 
       (mul-interval x  
                     (make-interval (/ 1.0 (upper-bound y)) 
                                    (/ 1.0 (lower-bound y)))))) 