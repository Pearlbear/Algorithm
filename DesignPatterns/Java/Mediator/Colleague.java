public abstract class Colleague
{
    private Mediator mediator = null;

    public Colleague(Mediator mediator)
    {
	this.mediator = mediator;
    }

    public Mediator getMediator()
    {
	return this.mediator;
    }
}
