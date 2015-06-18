/*
  如果要防止外部直接new Product，可以把Builder放在Product类里面作为内部类，私有化Product的构造方法，这样可以让外部只从Builder里面生成产品，保证产品的完整性。
  将ConcreteBuilder的创建放在这里是为了让Director和Builder脱耦，让导演者可以操纵多个Builder

使用场景：
1.产品类有复杂的内部结构，很多组成部分
2.产品类的组成部分相互依赖，有复杂的先后创建顺序
 */
public class Client
{
    public static void main(String[] args)
    {
	Builder builder = new ConcreteBuilder();

	Director director = new Director(builder);

	director.construct();

	Product product = builder.retriveProduct();
    }
}
