#include <iostream>
#include <thread>
#include <vector>
using namespace std;

//Function to be executed by multiple threads
void printHello(int threadId) {
    cout << "Hello from thread " << threadId << endl;
}

int main() {
    int myInt = 5;
    float myFloat = 5.99;
    double myDouble = 9.99;
    char myChar = 'A';
    bool myBool = true;

    cout << "Integer: " << myInt << endl;

    //Variables
    int a = 10;
    float b = 15.5;
    char c = 'C';

    cout << "\nVariable a: " << a << endl;

    //Operators
    int sum = a + myInt;
    int difference = a - myInt;
    int product = a * myInt;
    int quotient = a / myInt;
    int remainder = a % myInt;

    cout << "\nSum: " << sum << endl;
    cout << "Difference: " << difference << endl;
    cout << "Product: " << product << endl;
    cout << "Quotient: " << quotient << endl;
    cout << "Remainder: " << remainder << endl;

    bool isTrue = (a > myInt) && (b > 10);
    bool isFalse = (a < myInt) || (b < 10);

    cout << "Logical AND: " << isTrue << endl;
    cout << "Logical OR: " << isFalse << endl;

    //Loops
    cout << "\nFor Loop: " << endl;
    for (int i = 0; i < 5; i++) {
        cout << "i = " << i << endl;
    }

    cout << "\nWhile Loop: " << endl;
    int j = 0;
    while (j < 5) {
        cout << "j = " << j << endl;
        j++;
    }

    cout << "\nDo-While Loop: " << endl;
    int k = 0;
    do {
        cout << "k = " << k << endl;
        k++;
    } while (k < 5);

    //Conditions
    cout << "\nConditions:" << endl;
    if (a > myInt) {
        cout << "a is greater than myInt" << endl;
    } else if (a == myInt) {
        cout << "a is equal to myInt" << endl;
    } else {
        cout << "a is less than myInt" << endl;
    }

    cout << "\nSwitch Case:" << endl;
    switch (myChar) {
        case 'A':
            cout << "myChar is A" << endl;
            break;
        case 'B':
            cout << "myChar is B" << endl;
            break;
        default:
            cout << "myChar is neither A nor B" << endl;
    }

    //Functions
    cout << "\nFunction Example:" << endl;
    int result = addNumbers(3, 4);
    cout << "Result of addition: " << result << endl;

    //Pointers
    int myNumber = 100;
    int* ptr = &myNumber;

    cout << "\nPointers:" << endl;
    cout << "Value of myNumber: " << myNumber << endl;
    cout << "Memory address of myNumber: " << ptr << endl;
    cout << "Value pointed to by ptr: " << *ptr << endl;

    //Input/Output
    cout << "\nInput/Output:" << endl;
    int userInput;
    cout << "Enter an integer: ";
    cin >> userInput;
    cout << "You entered: " << userInput << endl;

    //Multithreading
    cout << "\nMultithreading Example (Einfacher):" << endl;
    int numThreads = 5;
    vector<thread> threads;

    //Erstelle und starte die Threads
    for (int i = 0; i < numThreads; ++i) {
        threads.push_back(thread([i]() {
            cout << "Hello from thread " << i << endl;
        }));
    }

    //Warte auf alle Threads
    for (auto& t : threads) {
        t.join();
    }

    return 0;
}

int addNumbers(int x, int y) {
    return x + y;
}