/*
  装饰模式和适配器模式的区别在于装饰模式不改变接口，只增强功能（复写方法），而适配器模式是改变接口，但不改变功能。
  一般来说装饰模式都是半透明的，即允许装饰模式改变接口，增加方法，如此，半透明的装饰模式就是介于装饰模式和适配器模式之间了。
  优点：动态扩展对象
  缺点：会产生比继承关系更多的对象，查错变得困难
 */
public class Decorator implements Component
{
    private Component component = null;

    public Decorator(Component component)
    {
	this.component = component;
    }

    public void operation()
    {
	this.component.operation();
    }
}
