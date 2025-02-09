#lang planet neil/sicp
(define (make-queue)
  (let ((front-ptr '())
        (rear-ptr '()))
    (define (dispatch m)
      (cond ((eq? m 'empty-queue?)
             (null? front-ptr))
            ((eq? m 'front-queue)
             (if (null? front-ptr)
                 (error "Empty queue")
                 (car front-ptr)))
            ((eq? m 'insert-queue!)
             (lambda (item)
               (let ((new-pair (cons item '())))
                 (if (null? front-ptr)
                     (begin (set! front-ptr new-pair)
                            (set! rear-ptr new-pair)
                            front-ptr)
                     (begin (set-cdr! rear-ptr new-pair)
                            (set! rear-ptr new-pair)
                            front-ptr)))))
            ((eq? m 'delete-queue!)
             (if (null? front-ptr)
                 (error "Empty queue")
                 (begin (set! front-ptr (cdr front-ptr))
                        front-ptr)))
            (else (error "Unsupported operation!"))))
    dispatch))

(define (empty-queue? queue)
  (queue 'empty-queue?))
(define (front-queue queue)
  (queue 'front-queue))
(define (insert-queue! queue item)
  ((queue 'insert-queue!) item))
(define (delete-queue! queue)
  (queue 'delete-queue!))

(define q (make-queue))
(empty-queue? q)
(insert-queue! q 'a)
(insert-queue! q 'b)
(front-queue q)
(delete-queue! q)
(front-queue q)