/*
  解释器模式：类的行为模式，定义出其文法的一种表示，并提供一个解释器来解释这个语言中的句子。
 */
public interface Expression
{
    public boolean interpret(Context context);

    public boolean equals(Object obj);

    public int hashCode();

    public String toString();
}
