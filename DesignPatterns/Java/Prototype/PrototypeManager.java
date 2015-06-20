/*
  此处我使用了一个单例模式，但是作用有待商榷，原例未使用单例模式，而是使用了一个静态类和同步方法。
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
	    throw new Exception("无此原型");
	return prototype;
    }
}
