public class LazySingleton
{
    private static LazySingleton instance = null;

    private LazySingleton(){}
    /*
    public static synchronized LazySingleton getInstance()//线程不安全，加了同步后才是线程安全，但是降低效率
    {
	if(instance == null)
	    instance = new LazySingleton();
	return instance;
    }
    */
    public static LazySingleton getInstance()
    {
	if(instance == null)
	    {
		synchronized(LazySingleton.class)
		    {
			if(instance == null)
			    instance = new LazySingleton();
		    }
	    }
	return instance;
    }
}
