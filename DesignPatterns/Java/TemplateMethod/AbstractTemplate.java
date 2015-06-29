/*
  模板方法模式的关键在于子类继承时所复写的方法只能置换父类的可变部分，但是子类不能改变模板方法模式的顶级逻辑。即要分清楚哪些是不能复写的，哪些是必须复写的，哪些是可以复写的。
 */
public abstract class AbstractTemplate
{
    public void templateMethod()
    {
	abstractMethod();
	hookMethod();
	concreteMethod();
    }
    //抽象方法，子类必须实现
    protected abstract void abstractMethod();
    //钩子方法，有一个默认空实现，子类可以实现，一般以do开头
    protected void hookMethod(){}
    //具体方法，子类不能实现
    private final void concreteMethod()
    {

    }
}
