/*
  相对于透明模式来说，安全模式使得客户端不会错误地调用Leaf的聚集方法，因为Leaf根本没有这些方法，编译就会报错，但是这也使得Leaf和Composite具有不同的接口，在某些时候可能会做类型转换，不够方便。
 */
public interface Component
{
    public void printStruct(String preStr);
}
