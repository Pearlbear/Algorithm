public class DomainLogin implements Login
{
    public boolean verify(String name, String password)
    {
	if(...)
	    return false;
	return true;
    }
}
