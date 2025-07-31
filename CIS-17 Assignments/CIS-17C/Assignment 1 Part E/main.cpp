#include <iostream>

using namespace std;

void deleteS(char*);

int main() {
  char s[12] = "Mississippi";

  deleteS(s);

  cout << s << endl; //Prints "Miiippi"

  return 0;
}

void deleteS(char* str) {
    char* p = str; // Only one local pointer variable that is used to write to the string
    while (*str) { // While the string is not null
        if (*str != 's' && *str != 'S') { // If the character is not 's' or 'S'
            *p = *str; // Copy the character to the new string
            p++; // Increment the pointer to the next position
        }
        str++; // Increment the pointer to the next character
    }
    *p = '\0'; // Add a null terminator to the end of the string
}