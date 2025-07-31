#ifndef DICE_H
#define DICE_H

#include <vector>
using namespace std;

class Dice {
private:
    vector<int> rolls;
    int Size;
public:
    Dice(); // default constructor
    void roll100();
    void calculateRolls() const;
    void printDice() const;
};

#endif // DICE_H 