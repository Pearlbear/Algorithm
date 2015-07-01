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

    private class ConcreteIterator implements Iterator
    {
	private int index;

	private int size;

	public ConcreteIterator(Aggregate agg)
	{
	    this.index = 0;
	    this.size = objects.size();
	}

	public void first()
	{
	    this.index = 0;
	}

	public void next()
	{
	    if(this.index < this.size)
		this.index++;
	}

	public boolean isDone()
	{
	    return this.index >= this.size;
	}

	public Object currentItem()
	{
	    return objects[index];
	}
    }

}
