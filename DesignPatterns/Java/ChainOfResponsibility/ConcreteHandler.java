public class concreteHandler
{
    @Override
    public void handleRequest()
    {
	if(successor != null)
	    {
		successor.handleRequest();
		System.out.println("�Ź�����");
	    }
	else
	    System.out.println("��������");
    }
}
