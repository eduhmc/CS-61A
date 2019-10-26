; Sierpinski's Triangle (aka Sierpinski's Gasket).
(speed 0)
(rt 90)

(define (ccurve length n)
  (if (= n 0)
    (fd length)
    (begin
      (lt 45)
      (ccurve (/ length (sqrt 2)) (- n 1))
      (rt 90)
      (ccurve (/ length (sqrt 2)) (- n 1))
      (lt 45)
      ) ; begin
    ) ; if
  ) ; define

(setposition (* 0.9 (/ (screen_width) -4)) 0)
(bgcolor "black")
(color "white")
(ccurve (* 0.9 (/ (screen_width) 2)) 10)

