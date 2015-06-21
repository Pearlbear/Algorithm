public class Leaf extends Component
{
    public Leaf(String name)
    {
        super(name);
    }

    public void printStruct(String preStr)
    {
	System.out.println(preStr + "-" + this.name);
    }
}
