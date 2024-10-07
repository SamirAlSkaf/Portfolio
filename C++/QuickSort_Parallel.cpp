#include <iostream>
#include <vector>
#include <thread>

//Partitionierung
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            ++i;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);

        // Threads für links und rechts
        std::thread leftThread, rightThread;

        if (pivotIndex - 1 > low) {
            leftThread = std::thread(quickSort, std::ref(arr), low, pivotIndex - 1);
        }

        if (pivotIndex + 1 < high) {
            rightThread = std::thread(quickSort, std::ref(arr), pivotIndex + 1, high);
        }

        if (leftThread.joinable()) {
            leftThread.join();
        }
        if (rightThread.joinable()) {
            rightThread.join();
        }
    }
}

int main() {
    std::vector<int> arr = {34, 7, 23, 32, 5, 62, 32, 7, 45, 19};

    quickSort(arr, 0, arr.size() - 1);

    for (int i : arr) {
        std::cout << i << " ";
    }

    return 0;
}
