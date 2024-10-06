using System;

public class QuickSort
{
    public QuickSort()
    {
        int[] numbers = { 9, 7, 5, 11, 12, 2, 14, 3, 10, 6 };
        Console.WriteLine("Unsorted array:");
        PrintArray(numbers);

        QuickSortAlgorithm(numbers, 0, numbers.Length - 1);

        Console.WriteLine("Sorted array:");
        PrintArray(numbers);
    }

    private void QuickSortAlgorithm(int[] array, int low, int high)
    {
        if (low < high)
        {
            int pivotIndex = Partition(array, low, high);
            QuickSortAlgorithm(array, low, pivotIndex - 1);
            QuickSortAlgorithm(array, pivotIndex + 1, high);
        }
    }

    private int Partition(int[] array, int low, int high)
    {
        int pivot = array[high];
        int i = low - 1;

        for (int j = low; j < high; j++)
        {
            if (array[j] <= pivot)
            {
                i++;
                Swap(array, i, j);
            }
        }
        Swap(array, i + 1, high);
        return i + 1;
    }

    private void Swap(int[] array, int i, int j)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    private void PrintArray(int[] array)
    {
        foreach (int value in array)
        {
            Console.Write(value + " ");
        }
        Console.WriteLine();
    }
}
