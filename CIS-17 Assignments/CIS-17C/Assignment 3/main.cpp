#include <iostream> 
using namespace std; 

struct Node {  
    int value;  
    Node* next; 
}; 

class LinkedList {  
private:    
    Node* head;  
public:    
    LinkedList() {      
        //STUDENT COMPLETES THIS    
        head = nullptr;
    } 
    LinkedList(const LinkedList& old) {      
        //STUDENT COMPLETES THIS    
        head = nullptr;
        Node* current = old.head;
        while (current != nullptr) {
            addToRear(current->value);
            current = current->next;
        }
    } 
    ~LinkedList() {      
        //STUDENT COMPLETES THIS    
        Node* current = head;
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
        head = nullptr;
    } 
    LinkedList& operator=(const LinkedList& src) {      
        if (this == &src) return *this; // if src is itself, return the current list
        
        Node* current = head; // traverse the current list and delete each node,
        while (current != nullptr) {
            Node* temp = current; // store the current node
            current = current->next; // move to the next node
            delete temp; // delete the current node (not pointer) to free memory
        }
        head = nullptr;
        
        Node* srcCurrent = src.head; // traverse the source list and add each node to the current list 
        while (srcCurrent != nullptr) { 
            addToRear(srcCurrent->value); // copy over the value of the current node to the current list
            srcCurrent = srcCurrent->next; // move to the next node
        }
        
        return *this; 
    } 
    int size() {      
        //STUDENT COMPLETES THIS    
        int count = 0;
        Node* current = head;
        while (current != nullptr) {
            count++;
            current = current->next;
        }
        return count;
    }         
    void addToFront(int v) {      
        //STUDENT COMPLETES THIS    
        Node* newNode = new Node;
        newNode->value = v; 
        newNode->next = head; // set the new node's next to the current head node
        head = newNode; // set the head pointer to the new node
    } 
    void addToRear(int v) {      
        //STUDENT COMPLETES THIS    
        if (head == nullptr) {
            addToFront(v);
        } else {
            Node* current = head;
            while (current->next != nullptr) { // traverse until current points to the last node
                current = current->next;
            }
            Node* newNode = new Node;
            newNode->value = v;
            newNode->next = nullptr; // set the new node's next to nullptr to indicate it is the last node
            current->next = newNode; // set the last node's next to the new node
        }
    } 
    void deleteItem(int v) {      
        //STUDENT COMPLETES THIS   
        if (head == nullptr) { // if the list is empty
            return;
        }
        if (head->value == v) { // if the head node is the item to delete
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node* current = head;
        while (current != nullptr) {
            if (current->next != nullptr && current->next->value == v) {
                break; // current points to the node before the node to delete
            }
            current = current->next;
        }
        if (current != nullptr) { 
            Node* temp = current->next;
            current->next = temp->next;
            delete temp;
        }
    }
    void swapList(LinkedList& other) {      
        //STUDENT COMPLETES THIS    
        Node* temp = head; // store the head of the current list
        head = other.head; // set the head of the current list to the head of the other list
        other.head = temp; // set the head of the other list to the head of the current list
    }       
    void printItems() {      
        //STUDENT COMPLETES THIS    
        Node* current = head;
        while (current != nullptr) {
            cout << current->value << " ";
            current = current->next;
        }
        cout << endl;
    }    
}; 

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