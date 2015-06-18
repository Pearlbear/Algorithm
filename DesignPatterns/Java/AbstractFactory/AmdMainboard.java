public class AmdMainboard implements AbstractMainboard
{
    private int holes = null;

    public AmdMainboard(int holes)
    {
	this.holes = holes;
    }

    public void installCpu()
    {
	System.out.println("Ö÷°åµÄCPU²å²ÛÎª£º"+this.holes);
    }
}
