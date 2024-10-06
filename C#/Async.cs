using System;
using System.Threading.Tasks;

public class Async
{
    public Async()
    {
        RunAsync().Wait(); //Ruft die asynchrone Methode synchron auf, um sie im Konstruktor auszuführen
    }

    public async Task RunAsync()
    {
        Console.WriteLine("Start der asynchronen Methoden");

        //Starte zwei Aufgaben parallel
        Task task1 = Task1Async();
        Task task2 = Task2Async();

        //Warten, bis beide Aufgaben abgeschlossen sind
        await Task.WhenAll(task1, task2);

        Console.WriteLine("Ende der asynchronen Methoden");
    }

    private async Task Task1Async()
    {
        Console.WriteLine("Task1 gestartet");
        await Task.Delay(2000); //Simuliert eine Verzögerung von 2 Sekunden
        Console.WriteLine("Task1 beendet");
    }

    private async Task Task2Async()
    {
        Console.WriteLine("Task2 gestartet");
        await Task.Delay(3000); //Simuliert eine Verzögerung von 3 Sekunden
        Console.WriteLine("Task2 beendet");
    }
}
