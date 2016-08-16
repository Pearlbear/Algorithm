#lang planet neil/sicp
#|
(magnitude z)取的是('complex ('rectangular (x y))),如果不加入上述代码,那么取出的类型是'complex,在magnitude中没有定义,magnitude只能
取出类型为'rectangular或'polar的数据,所以无法取出.在加入了上述代码后,先取出'complex,然后再取出'rectangular,才能取到正确的类型.
被调用了两次,第一次分派到complex,第二次分派到rectangular
|#