/*
  复合享元模式：只有单纯的享元对象可以共享，复合的享元对象不可以共享。
 */
public interface Flyweight
{
    public void operation(String externalState);
}
