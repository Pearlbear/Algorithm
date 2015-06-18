public class ComputerEngineer
{
    private AbstractCpu cpu = null;
    private AbstractMainboard mainboard = null;

    public void makeComputer(AbstractFactory af)
    {
	this.cpu = af.produceCpu();
        
	this.mainboard = af.produceMainboard();

	this.cpu.calculate();
	this.mainboard.installCpu();
    }
}
