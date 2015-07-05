public class ConcreteStateB implements State
{
    public void handle(Context context)
    {
	System.out.println("StateB"+context.toString());
    }
}
