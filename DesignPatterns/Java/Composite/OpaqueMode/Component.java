/*
  更建议使用透明模式，因为更符合Composite模式的理念，因为Composite的理念是：让调用者不用区分操作的是树叶对象还是树枝对象，而是以一个统一的方式来操作。
 */
public abstract class Component
{
    protected String name = null;

    public Component(String name)//这两步是否需要视情况而定，因为会增加耦合性，导致子类不易修改
    {
    	this.name = name;
    }
    
    public abstract void printStruct(String preStr);

    public void addChild(Component child)
    {
	throw new UnsupportedOperationException("不支持的操作");
    }

    public void removeChild(int index)
    {
	throw new UnsupportedOperationException("不支持的操作");
    }

    public List<Component> getChild()
    {
	throw new UnsupportedOperationException("不支持的操作");
    }

    
}
