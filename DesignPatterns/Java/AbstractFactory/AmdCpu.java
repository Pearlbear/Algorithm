public class AmdCpu implements AbstractCpu
{
    private int pins = null;

    public AmdCpu(int pins)
    {
	this.pins = pins;
    }

    public void calculate()
    {
	System.out.println("CPU�������Ϊ��"+this.pins);
    }
}
