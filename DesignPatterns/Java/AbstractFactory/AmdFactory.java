public class AmdFactory implements AbstractFactory
{
    public AbstractCpu produceCpu()
    {
	return new AmdCpu(1050);
    }
    public AbstractMainboard produceMainboard()
    {
	return new AmdMainboard(1050);
    }
}
