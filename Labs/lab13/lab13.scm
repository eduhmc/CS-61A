; Lab 13: Final Review

; Q3
(define (compose-all funcs)
  (if (null? funcs)
  	(lambda (x) x)
  	(lambda (x) 
  		((compose-all (cdr funcs)) ((car funcs) x)))
  	)
)