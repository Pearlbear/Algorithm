/*
  享元模式采用一个共享来避免大量拥有相同内容对象的开销，主要是内存开销。
  内蕴状态：享元对象内部不会随环境改变而改变的参数。
  外蕴状态：当需要用到享元对象时再传入的参数，随外部环境改变而改变。
  单纯享元模式：所有享元对象都是可以共享的。
 */
public interface Flyweight
{
    public void operation(String externalState);
}
