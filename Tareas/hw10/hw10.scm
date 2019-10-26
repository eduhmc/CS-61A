(define (accumulate combiner start n term)
  (if (= n 0) 
  	start
  	(accumulate combiner (combiner start (term n)) (- n 1) term))
)

(define (accumulate-tail combiner start n term)
  (if (= n 0) 
  	start
  	(accumulate combiner (combiner start (term n)) (- n 1) term))
)

(define (rle s)
  (define (helper-1 stream my-num counter)
  	(if (or (null? stream)(not(= my-num (car stream))))
  	counter
  	(helper-1 (cdr-stream stream) my-num (cons my-num(cons (+ (car (cdr counter)) 1) nil)))
  )
)
(define (helper-2 stream my-num)
	(if (null? stream)
		nil
		(if (= (car stream) my-num)
		(helper-2 (cdr-stream stream) my-num)
		stream
		)
	)
)
(if (null? s)
	nil

	(cons-stream (helper-1 (cdr-stream s)(car s) (list(car s)1)) (rle (helper-2 s (car s))))
	)
)