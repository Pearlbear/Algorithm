#lang planet neil/sicp
#|
正则序：
(gcd 206 40)
(gcd 40 (remainder 206 40))
(if (= (remainder 206 40) 0) ...)
    40
    (gcd (remainder 206 40) (remainder 40 (remainder 206 40))) 
(if (= (remainder 40 (remainder 206 40)) 0) ...)
    (gcd (remainder 40 (remainder 206 40)) (remainder (remainder 206 40) (remainder 40 (remainder 206 40)))))
(if (= (remainder (remainder 206 40) (remainder 40 (remainder 206 40))) ...)
...
18次remainder运算
---
应用序：
(gcd 206 40)
(gcd 40 (remainder 206 40))
(gcd 40 6)                     <--
(gcd 6 (remainder 40 6)) 
(gcd 6 4)                      <--
(gcd 4 (remainder 6 4)) 
(gcd 4 2)                      <--
(gcd 2 (remainder 4 2)) 
(gcd 2 0)                      <--
4次
|#