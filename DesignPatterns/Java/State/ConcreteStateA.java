public class ConcreteStateA implements State
{
    public void handle(Context context)
    {
	System.out.println("StateA"+context.toString());
    }
}
