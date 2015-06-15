public class LoginFactory
{
    public static Login getLogin(String type)
    {
	if(type.equals("domain"))
	    {
		return new DomainLogin();
	    }
	else
	    return new PasswordLogin();
    }
}
