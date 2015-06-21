public class Composite implements Component
{
    private String name = null;

    private List<Component> childComponents = new ArrayList<Component>();
    
    public Composite(String name)
    {
	this.name = name;
    }

    public void addChild(Component child)
    {
	childComponents.add(child);
    }

    public void removeChild(int index)
    {
	childComponents.remove(index);
    }

    public List<Component> getChild()
    {
	return childComponents;
    }

    public void printStruct(String preStr)
    {
	System.out.println(preStr + "-" + this.name);

	if(this.childComponents != null)
	    {
		preStr += "  ";
		for(Component child:childComponents)
		    {
			child.printStruct(preStr);
		    }
	    }
    }
}
