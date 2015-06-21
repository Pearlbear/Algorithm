public class Composite extends Component
{
    private List<Component> childComponents = new ArrayList<Component>();
    
    public Composite(String name)
    {
	super(name);
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
