/*
  
 */
public class Decorator implements Component
{
    private Component component = null;

    public Decorator(Component component)
    {
	this.component = component;
    }

    public void operation()
    {
	this.component.operation();
    }
}
