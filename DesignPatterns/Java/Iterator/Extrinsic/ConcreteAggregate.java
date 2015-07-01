public class ConcreteAggregate implements Aggregate
{
    private Object[] objects = null;

    public ConcreteAggregate(Object[] objects)
    {
	this.objects = objects;
    }

    public Iterator createIterator()
    {
	return new ConcreteIterator(this);
    }

    public Object getElement(int index)
    {
	if(index < objects.length)
	    {
		return objects[index];
	    }
	else
	    return null;
    }

    public int size()
    {
	return objects.length;
    }
}
