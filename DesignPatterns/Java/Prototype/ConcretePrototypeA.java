public class ConcretePrototypeA implements Prototype
{
    private String name = null;
    
    public Prototype clone()
    {
	Prototype prototype = new ConcretePrototypeA();
	prototype.setName(this.name);
	return prototype;
    }

    public String toString()
    {
	return "PrototypeA,name = "+this.name;
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
