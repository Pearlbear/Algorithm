public class ConcreteIterator implements Iterator
{
    private Aggregate agg = null;

    private int index;

    private int size;

    public ConcreteIterator(Aggregate agg)
    {
	this.agg = agg;
	this.index = 0;
	this.size = agg.size();
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
	return agg.getElement(this.index);
    }
}
