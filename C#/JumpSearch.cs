using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        int[] arr = { 1, 4, 7, 10, 13, 16, 19, 22, 25, 28 };
        int x = 19; //Wert, den wir suchen

        JumpSearch js = new JumpSearch();
        int result = await js.SearchAsync(arr, x);

        if (result != -1)
            Console.WriteLine($"Element {x} gefunden an Index {result}");
        else
            Console.WriteLine($"Element {x} nicht gefunden");
    }
}

class JumpSearch
{
    public async Task<int> SearchAsync(int[] arr, int x)
    {
        return await Task.Run(() => Search(arr, x));
    }

    private int Search(int[] arr, int x)
    {
        int n = arr.Length;
        int step = (int)Math.Sqrt(n); 
        int prev = 0;

        //Finden des Block, in dem das Element sein könnte
        while (arr[Math.Min(step, n) - 1] < x)
        {
            prev = step;
            step += (int)Math.Sqrt(n);
            if (prev >= n)
                return -1;
        }

        //Lineare Suche im gefundenen Block
        for (int i = prev; i < Math.Min(step, n); i++)
        {
            if (arr[i] == x)
                return i;
        }

        return -1;
    }
}
