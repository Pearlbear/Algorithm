public class Leaf implements Component
{
    private String name = null;

    public Leaf(String name)
    {
	this.name = name;
    }

    public void printStruct(String preStr)
    {
	System.out.println(preStr + "-" + this.name);
    }
}
