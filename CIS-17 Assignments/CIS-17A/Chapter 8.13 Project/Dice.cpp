#include "Dice.h"
#include <iostream>
#include <cstdlib>
// #include <ctime>
using namespace std;

// Default constructor: sets all values of the vector to 0
Dice::Dice() {
    Size = 100;
    rolls.resize(Size, 0);
}

// Rolls the die 100 times and records each roll in the vector
void Dice::roll100() {
    // srand(time(0));
    for (int i = 0; i < Size; i++) {
        rolls[i] = (rand() % 6) + 1;
    }
}

// Calculates and displays the number of each roll (1-6)
void Dice::calculateRolls() const {
    int counts[6] = {0};
    for (int i = 0; i < Size; i++) {
        if (rolls[i] >= 1 && rolls[i] <= 6)
            counts[rolls[i] - 1]++;
    }
    for (int i = 0; i < 6; i++) {
        cout << "Number of " << (i+1) << "s: " << counts[i] << endl;
    }
}

// Prints the contents of the vector, 10 elements per line
void Dice::printDice() const {
    for (int i = 0; i < Size; i++) {
        cout << rolls[i] << " ";
        if ((i+1) % 10 == 0)
            cout << endl;
    }
} 