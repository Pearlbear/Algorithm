public class ConcreteObserver implements Observer
{
    //����һ����subject�����ã���������Ҫ����ʱֱ�ӴӸ������л�ȡ
    private Subject subject = null;

    public void update(Subject subject)
    {
	this.subject = subject;
    }
}
