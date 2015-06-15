public class PasswordLogin implements Login
{
    public boolean verify(String name, String password)
    {
	if(...)
	    return false;
	return true;
    }
}
