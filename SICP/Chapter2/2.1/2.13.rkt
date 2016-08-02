#lang racket
#|
a*b
=(Ca*(1-Wa), Ca*(1+Wa)) * (Cb*(1-Wb), Cb*(1+Wb))
=(Ca*Cb*(1-Wa-Wb+Wa*Wb), Ca*Cb*(1+Wa+Wb+Wa*Wb)
误差很小,因此Wa*Wb可以忽略
=(Ca*Cb*(1-Wa-Wb), Ca*Cb*(1+Wa+Wb))
|#