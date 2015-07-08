/*
  调停者模式：把多个对象间的交互封装到Mediator里面，使得对象间松散耦合，从多对多变成一对多。
 */
public interface Mediator
{
    public void changed();
}
