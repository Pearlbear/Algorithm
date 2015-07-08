public class ConcreteMediator implements Mediator
{
    private ConcreteColleagueA concreteColleagueA = null;

    private ConcreteColleagueB concreteColleagueB = null;

    public void setColleagueA(ConcreteColleagueA concreteColleagueA)
    {
	this.concreteColleagueA = concreteColleagueA;
    }

    public void setColleagueB(ConcreteColleagueB concreteColleagueB)
    {
	this.concreteColleagueB = concreteColleagueB;
    }

    public void changed(Colleague colleague)
    {
	
    }
}
