/*
  ������ģʽ�������Ϊģʽ����������ķ���һ�ֱ�ʾ�����ṩһ����������������������еľ��ӡ�
 */
public interface Expression
{
    public boolean interpret(Context context);

    public boolean equals(Object obj);

    public int hashCode();

    public String toString();
}
