public class IntelMainboard implements AbstractMainboard
{
    private int holes = null;

    public IntelMainboard(int holes)
    {
	this.holes = holes;
    }

    public void installCpu()
    {
	System.out.println("�����CPU���Ϊ��"+this.holes);
    }
}
