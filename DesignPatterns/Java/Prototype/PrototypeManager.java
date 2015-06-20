/*
  �˴���ʹ����һ������ģʽ�����������д���ȶ��ԭ��δʹ�õ���ģʽ������ʹ����һ����̬���ͬ��������
 */

public enum PrototypeManager
{
    PM;
    
    private Map<String, Prototype> prototypes = null;

    private PrototypeManager()
    {
	prototypes = new HashMap<String, Prototype>();
    }

    public void addPrototype(String id, Prototype prototype)
    {
	prototypes.put(id, prototype);
    }

    public void removePrototype(String id)
    {
        prototypes.remove(id);
    }

    public Prototype getPrototype(String id) throws Exception
    {
	Prototype prototype = prototypes.get(id);
	if(prototype == null)
	    throw new Exception("�޴�ԭ��");
	return prototype;
    }
}
