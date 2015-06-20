/*
  登记式原型模式，通过克隆自身来创建一个新的对象，数据跟所克隆的对象一样，但是分为“浅克隆”和“深度克隆”，登记式通过一个第三方管理对象来管理所有克隆对象。
 */
public interface Prototype
{
    public Prototype clone();

    public String getName();

    public void setName();
}
