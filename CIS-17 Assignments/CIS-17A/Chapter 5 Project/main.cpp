#include <iostream>
#include <string>
using namespace std;

int main() { 
  double input1, input2, input3;
  cout << "Enter today's sales for store 1: "; 
  cin >> input1;
  cin.ignore();
  cout << "Enter today's sales for store 2: ";
  cin >> input2;
  cin.ignore();
  cout << "Enter today's sales for store 3: ";
  cin >> input3;
  cin.ignore();
  cout << "DAILY SALES\n(each*= $100)\n";
  
  // Round to nearest 100
  int rounded1 = (int)((input1 + 50) / 100) * 100;
  int rounded2 = (int)((input2 + 50) / 100) * 100;
  int rounded3 = (int)((input3 + 50) / 100) * 100;
  
  cout << "Store 1: "; for (int i = 0; i < rounded1 / 100; i++) cout << "*";
  cout << "\nStore 2: "; for (int i = 0; i < rounded2 / 100; i++) cout << "*";
  cout << "\nStore 3: "; for (int i = 0; i < rounded3 / 100; i++) cout << "*";
}