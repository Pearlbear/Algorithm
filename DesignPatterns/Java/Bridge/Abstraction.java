/*
  桥梁模式的优点：分离了抽象部分和实现部分，极大地提高了系统的灵活性；抽象部分和实现部分可以分别独立地扩展，而不会相互影响，从而大大提高了系统的可扩展性。
 */
public abstract class Abstraction
{
    private Implementor impl;

    public Abstraction(Implementor impl)
    {
	this.impl = impl;
    }

    public void operation()
    {
	impl.operationImpl();
    }
}
