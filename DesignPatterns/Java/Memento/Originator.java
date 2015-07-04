public class Originator
{
    private String state = null;

    public void SetState(String state)
    {
	this.state = state;
    }

    public String getState()
    {
	return this.state;
    }

    public MementoIF createMemento()
    {
	return new Memento(state);
    }

    public void restoreMemento(MementoIF memento)
    {
	this.state = ((Memento)memento).getState();
    }

    private class Memento implements MementoIF
    {
	private String state = null;

	private Memento(String state)
	{
	    this.state = state;
	}

	private String getState()
	{
	    return this.state;
	}

	private void setState(String state)
	{
	    this.state = state;
	}
    }
}
