/*
  װ��ģʽ��������ģʽ����������װ��ģʽ���ı�ӿڣ�ֻ��ǿ���ܣ���д����������������ģʽ�Ǹı�ӿڣ������ı书�ܡ�
  һ����˵װ��ģʽ���ǰ�͸���ģ�������װ��ģʽ�ı�ӿڣ����ӷ�������ˣ���͸����װ��ģʽ���ǽ���װ��ģʽ��������ģʽ֮���ˡ�
  �ŵ㣺��̬��չ����
  ȱ�㣺������ȼ̳й�ϵ����Ķ��󣬲��������
 */
public class Decorator implements Component
{
    private Component component = null;

    public Decorator(Component component)
    {
	this.component = component;
    }

    public void operation()
    {
	this.component.operation();
    }
}
