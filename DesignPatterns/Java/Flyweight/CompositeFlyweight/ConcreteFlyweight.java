public class ConcreteFlyweight
{
    private Character internalState = null;

    public ConcreteFlyweight(Character internalState)
    {
	this.internalState = internalState;
    }

    @Override
    public void operation(String externalState)
    {
	System.out.println("ExternalState=" + externalState);
	System.out.println("InternalState=" + internalState);
    }
}
