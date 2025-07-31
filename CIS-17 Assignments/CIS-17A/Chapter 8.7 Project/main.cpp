#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "*********************************************" << endl;
    cout << "This program displays to a user the total sales" << endl;
    cout << "of 5 different salsas!" << endl;
    cout << "*********************************************" << endl;

    const int NUM_SALSAS = 5;
    string salsaNames[NUM_SALSAS] = {"mild", "medium", "sweet", "hot", "zesty"};
    int sales[NUM_SALSAS];

    // Input: Get sales for each salsa type
    for (int i = 0; i < NUM_SALSAS; i++) {
        do {
            cout << "Enter the amount of jars sold for " << salsaNames[i] << " salsa: " << endl;
            cin >> sales[i];
            if (sales[i] < 0) {
                cout << "Sales cannot be negative. Please enter again." << endl;
            }
        } while (sales[i] < 0);
    }

    cout << "\n*********************************************" << endl;;
    int totalSales = 0;
    int highestIndex = 0;
    int lowestIndex = 0;

    // Display sales for each type and calculate total, highest, and lowest
    for (int i = 0; i < NUM_SALSAS; i++) {
        cout << "The total sales for " << salsaNames[i] << " salsa: " << sales[i] << endl;
        totalSales += sales[i];
        if (sales[i] > sales[highestIndex]) highestIndex = i;
        if (sales[i] < sales[lowestIndex]) lowestIndex = i;
    }
    cout << "----------------------------------------------" << endl;
    cout << "Highest selling salsa: " << salsaNames[highestIndex] << endl;
    cout << "Lowest selling salsa: " << salsaNames[lowestIndex] << endl;
    cout << "Total sales of the salsas: " << totalSales << endl;
    cout << "*********************************************" << endl;

    return 0;
}