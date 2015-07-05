public class Context
{
    private State state = null;

    public void setState(State state)
    {
	this.state = state;
    }

    public void request()
    {
	state.handle(this);
    }
}
