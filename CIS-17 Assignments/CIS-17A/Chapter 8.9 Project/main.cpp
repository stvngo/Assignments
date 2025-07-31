#include <iostream>
#include <cstdlib>
// #include <ctime>
using namespace std;

// Function to roll the die and fill the array
void rollDie(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = (rand() % 6) + 1; // random number between 1 and 6
    }
}

// Functions to count each die face
int numOnes(const int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (arr[i] == 1) count++;
    return count;
}

int numTwos(const int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (arr[i] == 2) count++;
    return count;
}

int numThrees(const int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (arr[i] == 3) count++;
    return count;
}

int numFours(const int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (arr[i] == 4) count++;
    return count;
}

int numFives(const int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (arr[i] == 5) count++;
    return count;
}

int numSixes(const int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (arr[i] == 6) count++;
    return count;
}

int main() {
    const int NUM_ROLLS = 100;
    int rolls[NUM_ROLLS];

    // srand(time(0));

    rollDie(rolls, NUM_ROLLS);

    cout << "Results of 100 rolls of a 6-sided die:" << endl;
    cout << "Number of Ones:   " << numOnes(rolls, NUM_ROLLS) << endl;
    cout << "Number of Twos:   " << numTwos(rolls, NUM_ROLLS) << endl;
    cout << "Number of Threes: " << numThrees(rolls, NUM_ROLLS) << endl;
    cout << "Number of Fours:  " << numFours(rolls, NUM_ROLLS) << endl;
    cout << "Number of Fives:  " << numFives(rolls, NUM_ROLLS) << endl;
    cout << "Number of Sixes:  " << numSixes(rolls, NUM_ROLLS) << endl;

    return 0;
}