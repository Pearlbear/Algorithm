public class Adapter implements Target
{
    private Adaptee adaptee = null;
    
    public Adapter(Adaptee adaptee)
    {
	this.adaptee = adaptee;
    }

    public void operation1()
    {
	this.adaptee.operation1();
    }

    public void operation2()
    {
	System.out.println("operation2()");
    }
}
