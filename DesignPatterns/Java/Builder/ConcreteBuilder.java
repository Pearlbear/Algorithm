public class ConcreteBuilder implements Builder
{
    private Product product = new Product();
    
    public void buildPart1()
    {
	product.setPart1("part1");
    }

    public void buildPart2()
    {
	product.setPart2("part2");
    }

    public Product retriveProduct()
    {
	return product;
    }
}
