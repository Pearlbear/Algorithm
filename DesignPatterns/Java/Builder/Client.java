/*
  ���Ҫ��ֹ�ⲿֱ��new Product�����԰�Builder����Product��������Ϊ�ڲ��࣬˽�л�Product�Ĺ��췽���������������ⲿֻ��Builder�������ɲ�Ʒ����֤��Ʒ�������ԡ�
  ��ConcreteBuilder�Ĵ�������������Ϊ����Director��Builder����õ����߿��Բ��ݶ��Builder

ʹ�ó�����
1.��Ʒ���и��ӵ��ڲ��ṹ���ܶ���ɲ���
2.��Ʒ�����ɲ����໥�������и��ӵ��Ⱥ󴴽�˳��
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
