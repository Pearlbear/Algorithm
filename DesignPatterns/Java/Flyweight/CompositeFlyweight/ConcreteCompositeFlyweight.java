public class ConcreteCompositeFlyweight implements Flyweight
{
    private Map<Character, Flyweight> flies = new HashMap<Character, Flyweight>();

    public void add(Character key, Flyweight fly)
    {
	flies.put(key, fly);
    }
    
    public void operation(String externalState)
    {
	Flyweight fly = null;
	for(Object o: flies.keySet())
	    {
		fly = flies.get(o);
		fly.operation(externalState);
	    }
    }
}
