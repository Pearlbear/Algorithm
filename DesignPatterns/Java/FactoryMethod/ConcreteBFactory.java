public class ConcreteBFactory implements AbstractFactory
{
    public AbstractProduct factory(String type)
    {
	if("A".equals(type))
	    {
		return new ConcreteBAProduct();
	    }
	else if("B".equals(type))
	    {
		return new ConcreteABProduct();
	    }
	else
	    return new RuntimeException("Î´ÖªÀàÐÍ");
    }
}
