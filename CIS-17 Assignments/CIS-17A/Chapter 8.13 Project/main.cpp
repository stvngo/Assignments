#include <iostream>
#include "Dice.h"
using namespace std;

int main() {
    Dice d;
    cout << "Initial dice vector (should be all 0s):" << endl;
    d.printDice();
    cout << endl;

    cout << "\nRolling the die 100 times..." << endl;
    d.roll100();
    cout << "\nDice vector after rolling:" << endl;
    d.printDice();
    cout << endl;

    cout << "\nCalculating the number of each roll:" << endl;
    d.calculateRolls();

    return 0;
}
