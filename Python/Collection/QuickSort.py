def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, high)
    return i + 1

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def print_array(array):
    print(array)

# Hauptfunktion
if __name__ == "__main__":
    numbers = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    print("Unsortiertes Array:")
    print_array(numbers)

    quick_sort(numbers, 0, len(numbers) - 1)

    print("Sortiertes Array:")
    print_array(numbers)
