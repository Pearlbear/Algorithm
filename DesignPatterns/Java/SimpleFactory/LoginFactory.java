public class LoginFactory
{
    public static Login factory(String type)
    {
	if(type.equals("domain"))
	    {
		return new DomainLogin();
	    }
	else
	    return new PasswordLogin();
    }
}
