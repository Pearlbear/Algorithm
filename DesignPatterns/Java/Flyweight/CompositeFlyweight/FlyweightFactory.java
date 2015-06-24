public enum FlyweightFactory
{
    Singleton;

    private Map<Character, Flyweight> flies = new HashMap<Character, Flyweight>();

    public Flyweight produce(Character internalState)
    {
	Flyweight fly = flies.get(internalState);

	if(fly == null)
	    {
		fly = new ConcreteFlyweight(internalState);
		flies.put(internalState, fly);
	    }

	return fly;
    }

    public Flyweight produce(List<Character> compositeInternalState)
    {
	ConcreteCompositeFlyweight compositeFly = new ConcreteCompositeFlyweight();
	for(Character internalState: compositeInternalState)
	    {
		compositeFly.add(internalState, this.produce(internalState));
	    }
	return compositeFly;
    }
}
