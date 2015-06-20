public class ConcretePrototypeB implements Prototype
{
    private String name = null;

    public Prototype clone()
    {
	Prototype prototype = new ConcretePrototypeB();
	prototype.setName(this.name);
	return prototype;
    }

    public String toString()
    {
	return "PrototypeB,name = "+this.name;
    }
    
    public String getName()
    {
	return this.name;
    }

    public void setName(String name)
    {
	this.name = name;
    }
}
