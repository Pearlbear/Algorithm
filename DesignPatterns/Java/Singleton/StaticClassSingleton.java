/*
  非常好的一种方式，不会因为同步而丢失效率，同时采用类级内部类的方式实现了线程安全
  只要不用到getInstance方法，那么SingletonHolder类就不会被初始化，节省了空间（我认为在此处已经声明了SingletonHolder，只是没有初始化）
 */
public class StaticClassSingleton
{
    private StaticClassSingleton(){}

    private static class SingletonHolder
    {
	private static StaticClassSingleton instance = new StaticClassSingleton();
    }

    public static StaticClassSingleton getInstance()
    {
	return SingletonHolder.instance;
    }
}
