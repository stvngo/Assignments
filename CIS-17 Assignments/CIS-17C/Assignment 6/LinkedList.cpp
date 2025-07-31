#include "LinkedList.h"
#include <iostream>

using namespace std;

// Constructor
LinkedList::LinkedList() {
    head = nullptr;
}

// Copy constructor
LinkedList::LinkedList(const LinkedList& old) {
    head = nullptr;
    if (old.head != nullptr) {
        head = copyListRecursive(old.head);
    }
}

// Destructor
LinkedList::~LinkedList() {
    deleteRecursive(head);
    head = nullptr;
}

// Assignment operator
LinkedList& LinkedList::operator=(const LinkedList& src) {
    if (this == &src) return *this;
    
    // Delete current list
    deleteRecursive(head);
    head = nullptr;
    
    // Copy from source
    if (src.head != nullptr) {
        head = copyListRecursive(src.head);
    }
    
    return *this;
}

// Public size function
int LinkedList::size() {
    return getSizeRecursive(head);
}

// Public addToFront function
void LinkedList::addToFront(int v) {
    Node* newNode = new Node;
    newNode->value = v;
    newNode->next = head;
    head = newNode;
}

// Public addToRear function
void LinkedList::addToRear(int v) {
    if (head == nullptr) {
        addToFront(v);
    } else {
        addToRearRecursive(head, v);
    }
}

// Public deleteItem function
void LinkedList::deleteItem(int v) {
    if (head == nullptr) {
        return;
    }
    
    if (head->value == v) {
        Node* temp = head;
        head = head->next;
        delete temp;
        deleteItem(v); // Recursively delete more instances
    } else {
        deleteItemRecursive(head, v);
    }
}

// Public swapList function
void LinkedList::swapList(LinkedList& Other) {
    swapListsRecursive(head, Other.head);
}

// Public printItems function
void LinkedList::printItems() {
    printListRecursive(head);
    cout << endl;
}

// Private recursive delete function
void LinkedList::deleteRecursive(Node* node) {
    if (node == nullptr) {
        return;
    }
    deleteRecursive(node->next);
    delete node;
}

// Private recursive copy function
Node* LinkedList::copyListRecursive(const Node* rhs) {
    if (rhs == nullptr) {
        return nullptr;
    }
    
    Node* newNode = new Node;
    newNode->value = rhs->value;
    newNode->next = copyListRecursive(rhs->next);
    return newNode;
}

// Private recursive print function
void LinkedList::printListRecursive(Node* node) {
    if (node == nullptr) {
        return;
    }
    cout << node->value << " ";
    printListRecursive(node->next);
}

// Private recursive size function
int LinkedList::getSizeRecursive(Node* node) {
    if (node == nullptr) {
        return 0;
    }
    return 1 + getSizeRecursive(node->next);
}

// Private recursive addToRear function
void LinkedList::addToRearRecursive(Node* node, int v) {
    if (node->next == nullptr) {
        Node* newNode = new Node;
        newNode->value = v;
        newNode->next = nullptr;
        node->next = newNode;
    } else {
        addToRearRecursive(node->next, v);
    }
}

// Private recursive deleteItem function
void LinkedList::deleteItemRecursive(Node* node, int v) {
    if (node == nullptr || node->next == nullptr) {
        return;
    }
    
    if (node->next->value == v) {
        Node* temp = node->next;
        node->next = temp->next;
        delete temp;
        deleteItemRecursive(node, v); // Continue deleting more instances
    } else {
        deleteItemRecursive(node->next, v);
    }
}

// Private recursive swapLists function
void LinkedList::swapListsRecursive(Node*& lhs, Node*& rhs) {
    // Base case: if both are null, nothing to swap
    if (lhs == nullptr && rhs == nullptr) {
        return;
    }

    // If one is null, move the other list over
    if (lhs == nullptr) {
        lhs = rhs;
        rhs = nullptr;
        return;
    }
    if (rhs == nullptr) {
        rhs = lhs;
        lhs = nullptr;
        return;
    }

    // Swap the current nodes' values
    int temp = lhs->value;
    lhs->value = rhs->value;
    rhs->value = temp;

    // Recursively swap the rest of the lists
    swapListsRecursive(lhs->next, rhs->next);
} 