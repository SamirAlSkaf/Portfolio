using System;
using System.Collections;

public class HashTable
{
    private Hashtable table;

    public HashTable()
    {
        //Initialisierung der Hashtable
        table = new Hashtable();
    }

    //Methode zum Hinzufügen von Elementen
    public void Add(string key, string value)
    {
        table.Add(key, value);
    }

    //Methode zum Abrufen von Elementen
    public string Get(string key)
    {
        return (string)table[key];
    }

    //Methode zum Ersetzen von Elementen
    public void Replace(string key, string newValue)
    {
        if (table.ContainsKey(key))
        {
            table[key] = newValue;
        }
        else
        {
            Console.WriteLine($"Schlüssel '{key}' existiert nicht.");
        }
    }

    //Methode zum Entfernen von Elementen
    public void Remove(string key)
    {
        table.Remove(key);
    }

    //Methode zum Überprüfen, ob ein Schlüssel existiert
    public bool ContainsKey(string key)
    {
        return table.ContainsKey(key);
    }

    //Methode zum Überprüfen auf Duplikate (gibt true zurück, wenn der Schlüssel bereits existiert)
    public bool Duplicate(string key)
    {
        return table.ContainsKey(key);
    }

    public static void Main(string[] args)
    {
        HashTable myHashTable = new HashTable();

        //Elemente hinzufügen
        myHashTable.Add("Name", "Alice");
        myHashTable.Add("Alter", "25");

        //Elemente abrufen
        Console.WriteLine("Name: " + myHashTable.Get("Name"));
        Console.WriteLine("Alter: " + myHashTable.Get("Alter"));

        //Ersetzen von Elementen
        myHashTable.Replace("Name", "Bob");
        Console.WriteLine("Name nach Replace: " + myHashTable.Get("Name"));

        //Überprüfen auf Duplikate
        Console.WriteLine("Hat Schlüssel 'Alter' Duplikate? " + myHashTable.Duplicate("Alter"));

        //Element entfernen
        myHashTable.Remove("Name");
        Console.WriteLine("Hat Schlüssel 'Name' nach Entfernen? " + myHashTable.ContainsKey("Name"));
    }
}
