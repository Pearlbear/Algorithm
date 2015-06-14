/*
  这是最有效率的方式，巧妙利用JVM解决了线程安全和节省空间的问题，而且非常简洁，很优美的实现
 */
public enum EnumSingleton
{
    Instance;

    public void operateSth()
    {
	//一些自定义功能
    }
}
