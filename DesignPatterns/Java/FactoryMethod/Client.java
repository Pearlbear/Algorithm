public class Client
{
    public static void main(String[] args)
    {
	AbstractFactory factory = new ConcreteAFactory();
	String type = "A";
	AbstractProduct product = factory.factory(type);
	product.function();
    }
}
