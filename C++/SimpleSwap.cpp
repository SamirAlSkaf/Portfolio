#include <iostream>
using namespace std;

//Swap without third variable
void swap(int* a, int* b) {
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

int main() {
    int x = 10, y = 20;

    cout << "Vor dem Swap: x = " << x << ", y = " << y << endl;

    swap(&x, &y);

    cout << "Nach dem Swap: x = " << x << ", y = " << y << endl;

    return 0;
}
