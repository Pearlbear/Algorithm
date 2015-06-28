public class Context
{
    private Strategy strategy = null;

    public Context(Strategy strategy)
    {
	this.strategy = strategy;
    }

    public void contextInterface()
    {
	this.strategy.strategyInterface();
    }
}
