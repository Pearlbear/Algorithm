public class IntelFactory implements AbstractFactory
{
    public AbstractCpu produceCpu()
    {
	return new IntelCpu(755);
    }
    public AbstractMainboard produceMainboard()
    {
	return new IntelMainboard(755);
    }
}
