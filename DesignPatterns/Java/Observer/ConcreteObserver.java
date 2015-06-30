public class ConcreteObserver implements Observer
{
    //保存一个对subject的引用，这样当需要数据时直接从该引用中获取
    private Subject subject = null;

    public void update(Subject subject)
    {
	this.subject = subject;
    }
}
