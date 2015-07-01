/*
  白箱聚集与外禀迭代子：将客户端与迭代子的责任分开，降低耦合性。
 */
public interface Iterator
{
    public void first();

    public void next();

    public boolean isDone();

    public Object currentItem();
}
