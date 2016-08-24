#lang racket
#|
acc的局部状态保存在E1的子环境里,acc2保存在E2的子环境里,由于有不同的子环境,所以局部状态是互不影响的;
会共享withdraw,deposit,dispatch的定义
|#