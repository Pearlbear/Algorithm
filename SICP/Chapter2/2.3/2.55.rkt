#lang planet neil/sicp
(car ''abracadabra)
#|
=>(car '(quote abracadabra))
car的对象是一个以quote和abracadabra为元素的表
所以结果是quote
类似于(car '(a b c))会返回a
|#