public void ProxyObject extends AbstractObject
{
    private RealObject ro = new RealObject();

    public void operation()
    {
	ro.operation();
    }
}
