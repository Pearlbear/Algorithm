/*
  ����ģʽ���ŵ㣺�����˳��󲿷ֺ�ʵ�ֲ��֣�����������ϵͳ������ԣ����󲿷ֺ�ʵ�ֲ��ֿ��Էֱ��������չ���������໥Ӱ�죬�Ӷ���������ϵͳ�Ŀ���չ�ԡ�
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
