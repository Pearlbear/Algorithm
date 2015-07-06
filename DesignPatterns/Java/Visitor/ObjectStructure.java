public class ObjectStructure
{
    private List<Node> nodes = new ArrayList<Node>();

    public void action(Visiton visitor)
    {
	for(Node node:nodes)
	    {
		node.accept(visitor);
	    }
    }

    public void add(Node node)
    {
	nodes.add(node);
    }
}
