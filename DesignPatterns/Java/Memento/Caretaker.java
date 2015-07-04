public class Caretaker
{
    private MementoIF memento = null;

    public void saveMemento(MementoIF memento)
    {
	this.memento = memento;
    }

    public MementoIF retrieveMemento()
    {
	return this.memento;
    }
}
