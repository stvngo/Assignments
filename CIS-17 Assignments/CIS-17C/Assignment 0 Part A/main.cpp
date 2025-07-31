

// Steven Ngo
// CIS 17C
// Assignment 0, Part A

#include <iostream>
#include <iomanip>

using namespace std;

double totalAmount(double array[], int size) {
  double total = 0.0;
  for (int i = 0; i < size; i++) {
      total += array[i];
  }
  return total;
}

double averageAmount(double array[], int size) {
  double total = totalAmount(array, size);
  return total / size;
}

double largestMonth(double array[], int size) {
  double largest = array[0];
  for (int i = 0; i < size; i++) {
      if (array[i] > largest) {
          largest = array[i];
      }
  }
  return largest;
}

double smallestMonth(double array[], int size) {
  double smallest = array[0];
  for (int i = 0; i < size; i++) {
      if (array[i] < smallest) {
          smallest = array[i];
      }
  }
  return smallest;
}

int main() {
  double creditCard[12];
  string months[12] = {"January", "February", "March", "April", "May", 
  "June", "July", "August", "September", "October", "November", "December"};
  
  cout << "Enter the credit card amounts for 12 months:\n";
  
  for (int i = 0; i < 12; i++) {
    cout << months[i] << ": $";
    cin >> creditCard[i];
    if (creditCard[i] < 0) {
        creditCard[i] = 0.0;  // Set negative values to 0
    }
  }
  
  cout << "\nHere are the credit card totals for each month:\n";
  cout << fixed << setprecision(2);
  
  for (int i = 0; i < 12; i++) {
      cout << left << setw(9) << months[i] << ": $" << creditCard[i] << endl;
  }
  
  // Display statistics
  cout << "\nThe total amount of money spent was $" << totalAmount(creditCard, 12) << endl;
  cout << "The average amount of money spent per month was $" << averageAmount(creditCard, 12) << endl;
  cout << "The most amount of money spent in a month was $" << largestMonth(creditCard, 12) << endl;
  cout << "The least amount of money spent in a month was $" << smallestMonth(creditCard, 12) << endl;
  
  return 0;
}