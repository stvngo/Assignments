#include <iostream> 
#include "LinkedList.h"
using namespace std; 

int main() {
    //LEAVE MAIN ALONE PLEASE!!!  <--NO REALLY...I MEAN IT!!!
  
    //Testing the addToRear function
    LinkedList L;
    L.addToRear(1);
    L.addToRear(2);
    L.addToRear(3);
    L.addToRear(5);
    L.addToRear(6);
    cout << "Testing addToRear()" << endl;
    L.printItems();
    cout << endl;
    cout << endl;
  
    //Testing the addToFront function
    L.addToFront(7);
    L.addToFront(8);
    cout << "Testing addToFront()" << endl;
    L.printItems();
    cout << endl;
    cout << endl;
  
    //Testing the size function
    cout << "The size of the list L is " << L.size() << endl;
    cout << endl;
    cout << endl;
  
    //Testing the copy constructor
    LinkedList LL(L);
    cout << "Testing the copy constructor" << endl;
    LL.printItems();
    cout << endl;
    cout << endl;
  
    //Testing the swapList function
    LinkedList LLL;
    LLL.addToFront(20);
    LLL.addToFront(30);
    LLL.addToFront(40);
    LLL.addToFront(50);
    LL.swapList(LLL);
    cout << "Testing swapList()" << endl;
    cout << "This is the output of LL" << endl;
    LL.printItems();
    cout << endl;
    cout << "This is the output of LLL" << endl;
    LLL.printItems();
    cout << endl;
    cout << endl;
  
    //Testing the assignment "=" operator
    L = LL = LLL;
    cout << "Testing the assignment \"=\" operator" << endl;
    cout << "This is the output of L" << endl;
    L.printItems();
    cout << endl;
    cout << "This is the output of LL" << endl;
    LL.printItems();
    cout << endl;
    cout << "This is the output of LLL" << endl;
    LLL.printItems();
    cout << endl;
    cout << endl;
  
    //Testing the deleteItem function
    LLL.deleteItem(3);
    LLL.deleteItem(5);
    cout << "Testing deleteItem()" << endl;
    LLL.printItems();
    cout << endl;
    cout << endl;
  
    //Testing the remainder of the deleteItem function
    LLL.deleteItem(1);
    LLL.deleteItem(2);
    LLL.deleteItem(6);
    LLL.deleteItem(7);
    LLL.deleteItem(8);
    cout << "This list should be empty" << endl;
    LLL.printItems();
    cout << "Yep...the list was empty" << endl;
    cout << endl;
    cout << endl;
  
    //Testing the destructor operator
    cout << "Testing the destructor" << endl;
    L.~LinkedList();
    cout << "Destructor called.  This program still runs." << endl;
}