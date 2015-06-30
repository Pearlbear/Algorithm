/*
  观察者模式是用来当被观察者更新时，通知所有的观察者自己的状态改变，由于腿模式固定了要传递的数据，因此难以复用，所以一般使用拉模式，即将自己的引用传递给观察者，当观察者需要时再自己从引用中获取数据。
 */
public interface Observer
{
    public void update(Subject subject);
}
