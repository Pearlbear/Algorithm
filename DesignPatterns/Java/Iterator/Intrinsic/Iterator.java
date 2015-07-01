/*
  黑箱聚集与内禀迭代子：阻止外部对聚集的直接访问，使得外部只能对迭代子对象进行操作
 */
public interface Iterator
{
    public void first();

    public void next();

    public boolean isDone();

    public Object currentItem();
}
