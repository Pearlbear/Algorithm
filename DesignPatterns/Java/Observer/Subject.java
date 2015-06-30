public abstract class Subject
{
    private List<Observer> observers = new ArrayList<Observer>();

    public void attach(Observer observer)
    {
	observer.update(this);//防止observer中使用时出现空指针
	
	observers.add(observer);
    }

    public void detach(Observer observer)
    {
	observers.remove(observer);
    }

    public void notifyObservers()
    {
	for(Observer observer:observers)
	    {
		observer.update(this);
	    }
    }
}
