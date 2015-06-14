public class LazySingleton
{
    private static LazySingleton instance = null;

    private LazySingleton(){}
    /*
    public static synchronized LazySingleton getInstance()//�̲߳���ȫ������ͬ��������̰߳�ȫ�����ǽ���Ч��
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
