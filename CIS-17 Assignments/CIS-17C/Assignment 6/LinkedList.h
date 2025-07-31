#ifndef LinkedList_h
#define LinkedList_h

#include "Node.h"

using namespace std;

class LinkedList {
private:
  Node* head;

  // Recursive helper functions
  void deleteRecursive(Node* node);
  Node* copyListRecursive(const Node* rhs);
  void printListRecursive(Node* node);
  int getSizeRecursive(Node* node);
  void addToRearRecursive(Node* node, int v);
  void deleteItemRecursive(Node* node, int v);
  void swapListsRecursive(Node*& lhs, Node*& rhs);

public:
  LinkedList();
  LinkedList(const LinkedList& old);
  ~LinkedList();
  LinkedList& operator=(const LinkedList& src);
  
  int size();
  void addToFront(int v);
  void addToRear(int v);
  void deleteItem(int v);
  void swapList(LinkedList& Other);
  void printItems();
};

#endif