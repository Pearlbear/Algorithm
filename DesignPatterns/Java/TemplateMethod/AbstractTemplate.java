/*
  ģ�巽��ģʽ�Ĺؼ���������̳�ʱ����д�ķ���ֻ���û�����Ŀɱ䲿�֣��������಻�ܸı�ģ�巽��ģʽ�Ķ����߼�����Ҫ�������Щ�ǲ��ܸ�д�ģ���Щ�Ǳ��븴д�ģ���Щ�ǿ��Ը�д�ġ�
 */
public abstract class AbstractTemplate
{
    public void templateMethod()
    {
	abstractMethod();
	hookMethod();
	concreteMethod();
    }
    //���󷽷����������ʵ��
    protected abstract void abstractMethod();
    //���ӷ�������һ��Ĭ�Ͽ�ʵ�֣��������ʵ�֣�һ����do��ͷ
    protected void hookMethod(){}
    //���巽�������಻��ʵ��
    private final void concreteMethod()
    {

    }
}
