#include <iostream>
#include "MyStack.h"

using namespace std;

int main() {
    
    //Test the MyStack() constructor and the printStack() & push(int) member functions
    cout << "I am testing MyStack(), printStack(), and push(int)" << endl;
    MyStack A;
    cout << "I am printing out the empty MyStack object A" << endl;
    A.printStack();
    cout << endl;
    A.push(1);
    A.push(2);
    A.push(3);
    A.push(4);
    A.push(5);
    A.push(6);
    cout << "I am printing out MyStack object A containing 6 5 4 3 2 1" << endl;
    A.printStack();
    cout << endl;
    cout << endl;

    //Test the copy constructor
    cout << "I am testing the MyStack copy constructor" << endl;
    MyStack B = A;
    cout << "I am printing out MyStack Object B containing 6 5 4 3 2 1" << endl;
    B.printStack();
    cout << endl;
    cout << endl;

    //Test the int peek() the int pop() and the int size() member functions
    cout << "I am testing peek: the top of the stack is " << A.peek() << endl;
    cout << "I didn't remove anything from the stack though...see" << endl;
    A.printStack();
    cout << endl;
    cout << "And the size of A is: " << A.size() << endl;
    cout << endl;
    cout << "Now I am testing pop: the item that I am removing is " << A.pop() << endl;
    cout << "So now 6 should be removed from the top of the stack..." << endl;
    A.printStack();
    cout << "And the size of A is: " << A.size() << endl;
    cout << endl;
    cout << endl;

    //Test the overloaded assignment operator
    cout << "Time to test the assignment (=) operator." << endl;
    A.pop();
    B = A;
    cout << "MyStack object B should now hold 4 3 2 1" << endl;
    B.printStack();
    cout << endl;
    cout << endl;

    //What happens when I try to peek into an empty stack?
    cout << "Let's Find out what happens when I peek or pop an empty MyStack" << endl;
    MyStack C;
    cout << "Here I try to peek into an empty stack " << C.peek() << endl;
    cout << "Here I try to pop from an empty stack " << C.pop() << endl;
    cout << endl;
    cout << endl;

    //Let's check the cascading effect of the overloaded assignment operator
    A.pop();
    A.pop();
    C = B = A;
    cout << "The contents of MyStack object A are:" << endl;
    A.printStack();
    cout << endl;
    cout << "The contents of MyStack object B are:" << endl;
    B.printStack();
    cout << endl;
    cout << "The contents of MyStack object C are:" << endl;
    C.printStack();
    cout << endl;
    cout << endl;

    //Let's Destroy a MyStack object a
    cout << "Testing the destructor" << endl;
    cout << "Destructor called" << endl;
    A.~MyStack();
    cout << "This program still runs" << endl;
}