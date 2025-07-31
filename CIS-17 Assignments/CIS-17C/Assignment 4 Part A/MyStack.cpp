#include "MyStack.h"
#include <iostream>
#include <climits>

MyStack::MyStack() {
    dummy.next = nullptr;
}

MyStack::MyStack(const MyStack& rhs) {
    dummy.next = nullptr;
    // Copy the linked list directly
    Node* current = rhs.dummy.next; // current is the pointer to the current node
    Node* tail = &dummy; // tail is the pointer to the last node in the new stack
    
    while (current != nullptr) {
        Node* newNode = new Node; // create a new node
        newNode->value = current->value; // set the value of the new node to the value of the current node
        newNode->next = nullptr; // set the next pointer of the new node to nullptr
        tail->next = newNode; // set the next pointer of the tail node to the new node
        tail = newNode; // set the tail node to the new node
        current = current->next; // move to the next node
    }
}

MyStack MyStack::operator=(const MyStack& rhs) {
    if (this == &rhs) { // if the stack is itself, return the stack
        return *this;
    }
    Node* current = dummy.next; // traverse the current stack and delete each node, current is the pointer to the current node
    while (current != nullptr) { 
        Node* temp = current; // store the current node
        current = current->next; // move to the next node
        delete temp; // delete the current node (not pointer) to free memory
    }
    dummy.next = nullptr;
    
    // Copy the linked list directly
    current = rhs.dummy.next;
    Node* tail = &dummy;
    
    while (current != nullptr) {
        Node* newNode = new Node;
        newNode->value = current->value;
        newNode->next = nullptr;
        tail->next = newNode;
        tail = newNode;
        current = current->next;
    }
    
    return *this;
}


void MyStack::push(int v) {
    Node* newNode = new Node;
    newNode->value = v;
    newNode->next = dummy.next; // new node points to current top
    dummy.next = newNode;        // dummy node points to new top
}

int MyStack::pop() {
    if (dummy.next == nullptr) {
        return INT_MIN;
    }
    Node* temp = dummy.next; // store the current top
    int value = temp->value; // store the value of the current top
    dummy.next = temp->next; // dummy node points to the next node
    delete temp; // delete the current top node to free memory
    return value;
}

int MyStack::peek() {
    if (dummy.next == nullptr) {
        return INT_MIN;
    }
    return dummy.next->value; // return the value of the current top
}

int MyStack::size() {
    Node* current = dummy.next; // traverse the stack and count the number of nodes
    int count = 0; // initialize the count to 0
    while (current != nullptr) {
        count++; // increment the count
        current = current->next; // move to the next node
    }
    return count;
}

void MyStack::printStack() {
    Node* current = dummy.next; // traverse the stack and print the value of each node
    while (current != nullptr) {
        cout << current->value << " "; // print the value of the current node
        current = current->next; // move to the next node
    }
    cout << endl;
}

MyStack::~MyStack() {
    Node* current = dummy.next; // traverse the stack and delete each node
    while (current != nullptr) {
        Node* temp = current; // store the current node
        current = current->next; // move to the next node
        delete temp; // delete the current node to free memory
    }
    dummy.next = nullptr;
}