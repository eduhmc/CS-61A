;;; DEMO1: Call expressions

(+ 1 2 3 4)
(+)
(*)
(- 12)
(- 20 1 2 3 4 5)
(* 2 (+ 1 (* 2 2 2 2 3 3 7)))
(number? 12)
(integer? 3.3)
(zero? 2)

;;; DEMO2: Definitions

(define (square x) (* x x))

(define (average x y) (/ (+ x y) 2))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (sqrt x)
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (= (square guess) x)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1))

;;; DEMO3: List demos

(cons 1 (cons 2 nil))
(define x (cons 1 (cons 2 nil)))
(car x)
(cdr x)
(car (cdr x))
(define (cadr lst) (car (cdr lst)))
(cadr x)
(cons 1 (cons 2 (cons 3 (cons 4 nil))))

(pair? x)
(pair? nil)
(null? x)
(null? nil)

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define squares (list 1 4 9 16 25))

(length squares)
