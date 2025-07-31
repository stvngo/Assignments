#include <iostream>
#include <climits>

#include "MyQueue.h"

MyQueue::MyQueue() {
    dummy.next = nullptr;
}

MyQueue::MyQueue(const MyQueue& rhs) {
    dummy.next = nullptr;
    Node* current = rhs.dummy.next;
    Node* tail = &dummy;
    while (current != nullptr) {
        Node* newNode = new Node;
        newNode->value = current->value;
        newNode->next = nullptr;
        tail->next = newNode;
        tail = newNode;
        current = current->next;
    }
}

MyQueue MyQueue::operator=(const MyQueue& rhs) {
    if (this == &rhs) {
        return *this;
    }
    Node* current = dummy.next;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }
    dummy.next = nullptr;
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

void MyQueue::push(int v) {
    Node* newNode = new Node;
    newNode->value = v;
    newNode->next = nullptr;
    
    if (dummy.next == nullptr) {
        // Queue is empty, add to front
        dummy.next = newNode;
    } else {
        // Queue has elements, find the last node
        Node* current = dummy.next;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }
}

int MyQueue::pop() {
    if (dummy.next == nullptr) {
        return INT_MIN;
    }
    Node* temp = dummy.next; // store the first node
    int value = temp->value; // store the value of the first node
    dummy.next = temp->next; // dummy node points to the next node
    delete temp; // delete the first node to free memory
    return value;
}

int MyQueue::peek() {
    if (dummy.next == nullptr) {
        return INT_MIN;
    }
    return dummy.next->value; // return the value of the first node
}

int MyQueue::size() {
    Node* current = dummy.next;
    int count = 0;
    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;
}

void MyQueue::printQueue() {
    Node* current = dummy.next; // traverse the stack and print the value of each node
    while (current != nullptr) {
        cout << current->value << " "; // print the value of the current node
        current = current->next; // move to the next node
    }
    cout << endl;
}

MyQueue::~MyQueue() {
    Node* current = dummy.next; // traverse the queue and delete each node
    while (current != nullptr) {
        Node* temp = current; // store the current node
        current = current->next; // move to the next node
        delete temp; // delete the current node to free memory
    }
    dummy.next = nullptr; // set the next pointer of the dummy node to nullptr
}