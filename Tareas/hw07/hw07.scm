(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car ( cdr s))
)

(define (caddr s)
  (car(cdr (cdr s)))
)

(define (sign x)
  (cond((> x 0) 1)
       ((< x 0) -1)
       ((= x 0) 0)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond((= n 1) b)
       (else (* b (pow b (- n 1))))
  )
)

(define (ordered? s)
  (cond ((null? s) #t)
        ((null? (cdr s)) #t)
        ((> (car s) (car (cdr s))) #f)
        (else (ordered? (cdr s)))
  )
)