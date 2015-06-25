/*
  门面模式的意义在于解耦功能和客户端，让客户端通过Facade调用功能，使得双方更好维护，同时让功能模块暴露希望暴露的方法
 */
public class Facade
{
    ModuleA a = new ModuleA();

    ModuleB b = new ModuleB();

    ModuleC c = new ModuleC();

    public void a1()
    {
	a.a1();
    }
    public void b1()
    {
	b.b1();
    }
    public void c1()
    {
	c.c1();
    }
}
