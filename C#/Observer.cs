using System;
using System.Collections.Generic;
using System.Xml.Linq;


public class Observer
{
    private List<Observer> observers = new List<Observer>();
    private string state;

    public string State
    {
        get { return state; }
        set 
        { 
            state = value;
            NotifyObservers();
        }
    }

    public void Attach(Observer observer)
    {
        observers.Add(observer);
    }

    public void Detach(Observer observer)
    {
        observers.Remove(observer);
    }

    public void NotifyObservers()
    {
        foreach (var observer in observers)
        {
            observer.Update();
        }
    }

    public virtual void Update()
    {
        Console.WriteLine($"Observer has received update: {state}");
    }
}

//ConcreteObserver
public class ConcreteObserver : Observer
{
    private string name;

    public ConcreteObserver(string name, Observer subject)
    {
        this.name = name;
        this.subject = subject;
        subject.Attach(this);
    }

    public override void Update()
    {
        Console.WriteLine($"{name} has received update: {subject.State}");
    }
}

//Main
public class Program
{
    public static void Main(string[] args)
    {
        Observer observer = new Observer();

        ConcreteObserver observer1 = new ConcreteObserver("Observer 1", observer);
        ConcreteObserver observer2 = new ConcreteObserver("Observer 2", observer);

        observer.State = "State 1";
        observer.State = "State 2";

        observer.Detach(observer1);

        observer.State = "State 3";
    }
}

