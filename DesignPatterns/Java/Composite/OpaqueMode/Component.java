/*
  ������ʹ��͸��ģʽ����Ϊ������Compositeģʽ�������ΪComposite�������ǣ��õ����߲������ֲ���������Ҷ��������֦���󣬶�����һ��ͳһ�ķ�ʽ��������
 */
public abstract class Component
{
    protected String name = null;

    public Component(String name)//�������Ƿ���Ҫ�������������Ϊ����������ԣ��������಻���޸�
    {
    	this.name = name;
    }
    
    public abstract void printStruct(String preStr);

    public void addChild(Component child)
    {
	throw new UnsupportedOperationException("��֧�ֵĲ���");
    }

    public void removeChild(int index)
    {
	throw new UnsupportedOperationException("��֧�ֵĲ���");
    }

    public List<Component> getChild()
    {
	throw new UnsupportedOperationException("��֧�ֵĲ���");
    }

    
}
