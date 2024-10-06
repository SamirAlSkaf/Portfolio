using System;
using System.Threading;

public class Multithreading
{
    public Multithreading()
    {
        //Erstelle und starte zwei Threads
        Thread thread1 = new Thread(new ThreadStart(DoWork));
        Thread thread2 = new Thread(new ThreadStart(DoWork));

        thread1.Start();
        thread2.Start();

        //Warte, bis beide Threads beendet sind
        thread1.Join();
        thread2.Join();

        //Ausgabe nach Abschluss beider Threads
        Console.WriteLine("Beide Threads sind beendet.");
    }

    private void DoWork()
    {
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} ist am Arbeiten.");
            Thread.Sleep(1000); //Simuliere Arbeit
        }
    }

    public static void Main(string[] args)
    {
        new Multithreading();
    }
}
