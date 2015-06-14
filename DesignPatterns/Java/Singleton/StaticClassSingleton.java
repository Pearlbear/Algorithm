/*
  �ǳ��õ�һ�ַ�ʽ��������Ϊͬ������ʧЧ�ʣ�ͬʱ�����༶�ڲ���ķ�ʽʵ�����̰߳�ȫ
  ֻҪ���õ�getInstance��������ôSingletonHolder��Ͳ��ᱻ��ʼ������ʡ�˿ռ䣨����Ϊ�ڴ˴��Ѿ�������SingletonHolder��ֻ��û�г�ʼ����
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
