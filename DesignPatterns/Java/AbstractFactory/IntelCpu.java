public class IntelCpu implements AbstractCpu
{
    private int pins = null;

    public IntelCpu(int pins)
    {
	this.pins = pins;
    }

    public void calculate()
    {
	System.out.println("CPU�������Ϊ��"+this.pins);
    }
}
