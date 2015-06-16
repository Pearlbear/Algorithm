public class Test
{
    public static void main(String[] args)
    {
	String name = "acmilan";
	String password = "111111";
	String type = "domain";

	Login login = LoginFactory.factory(type);
	boolean isRight = login.verify(name, password);
    }
}
