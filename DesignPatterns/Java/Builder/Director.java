public class Director
{
    private Builder builder = null;
    
    public Director(Builder builder)
    {
	this.builder = builder;
    }

    public void construct()
    {
	builder.buildPart1();
	builder.buildPart2();
    }
}
