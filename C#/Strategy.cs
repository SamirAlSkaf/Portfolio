using System;

//Strategy Interface
public interface IStrategy
{
    void Execute();
}

//Concrete Strategy A
public class ConcreteStrategyA : IStrategy
{
    public void Execute()
    {
        Console.WriteLine("Strategy A executed.");
    }
}

//Concrete Strategy B
public class ConcreteStrategyB : IStrategy
{
    public void Execute()
    {
        Console.WriteLine("Strategy B executed.");
    }
}

//Context Class
public class Strategy
{
    private IStrategy _strategy;

    public Strategy(IStrategy strategy)
    {
        _strategy = strategy;
    }

    public void SetStrategy(IStrategy strategy)
    {
        _strategy = strategy;
    }

    public void ExecuteStrategy()
    {
        _strategy.Execute();
    }
}


class Program
{
    static void Main()
    {
        //Create a Strategy object with a specific strategy
        Strategy strategyContext = new Strategy(new ConcreteStrategyA());
        strategyContext.ExecuteStrategy(); //Output: Strategy A executed.

        //Change the strategy at runtime
        strategyContext.SetStrategy(new ConcreteStrategyB());
        strategyContext.ExecuteStrategy(); //Output: Strategy B executed.
    }
}
