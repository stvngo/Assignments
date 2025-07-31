#include <iostream>

using namespace std;

double* addArrays(double* &arr1, double* &arr2, int ARRSIZE) {
  double* result = new double[ARRSIZE]; // allocate memory for the result array
  for (int i = 0; i < ARRSIZE; i++) {
    *(result + i) = *(arr1 + i) + *(arr2 + i); // pointer arithmetic
  }
  return result;
}

int main() {
  const int ARRSIZE = 10;
  double arr1[ARRSIZE] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0}; // initialize the arrays
  double arr2[ARRSIZE] = {10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0};
  
  double *ptr1 = arr1;
  double *ptr2 = arr2;
  double *numbers = nullptr;
  numbers = addArrays(ptr1, ptr2, ARRSIZE); // call the function
  cout << "Array 1:" << endl;
  for (int i = 0; i < ARRSIZE; i++) {
    cout << *(arr1 + i) << " ";
  }
  cout << endl;
  
  cout << "Array 2:" << endl;
  for (int i = 0; i < ARRSIZE; i++) {
    cout << *(arr2 + i) << " ";
  }
  cout << endl;
  
  cout << "Result Array (element-by-element addition):" << endl;
  for (int i = 0; i < ARRSIZE; i++) {
    cout << *(numbers + i) << " ";
  }
  cout << endl;
  
  delete[] numbers; // Clean up allocated memory
  return 0;
}