public abstract class Subject
{
    private List<Observer> observers = new ArrayList<Observer>();

    public void attach(Observer observer)
    {
	observer.update(this);//��ֹobserver��ʹ��ʱ���ֿ�ָ��
	
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
