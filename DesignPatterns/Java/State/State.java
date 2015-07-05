/*
  状态模式：让一个对象根据其内部状态改变而改变其行为
 */
public interface State
{
    //可以不传递Context对象，但是因为一般会回调Context中的数据，所以一般直接将Context的引用传递过来
    public void handle(Context context);
}
