public class concreteHandler
{
    @Override
    public void handleRequest()
    {
	if(successor != null)
	    {
		successor.handleRequest();
		System.out.println("放过请求");
	    }
	else
	    System.out.println("处理请求");
    }
}
