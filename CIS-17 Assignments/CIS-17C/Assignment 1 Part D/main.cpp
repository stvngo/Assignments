#include <iostream>
#include <cmath>
using namespace std;

// return true if two C strings are equal
bool match(const char str1[], const char str2[]) {
  // str1 and str2 are pointers to the first characters of the strings
  while (*str1 != '\0' && *str2 != '\0') { // zero bytes at ends
    if (*str1 != *str2) // compare corresponding chars
      return false;
    str1++; // advance to the next character
    str2++;
  }
  return *str1 == *str2;
  // return true if both strings ended at the same time
}

int main(){
  char a[10] = "pointy";
  char b[10] = "pointless";
  if (match(a,b))
    cout << "They're the same!\n";
  return 0;
}