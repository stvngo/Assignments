#include <iostream>
#include "StudentData.h"
using namespace std;

int main() {
    cout << "Testing StudentData constructor..." << endl;
    StudentData s("Doe", "John", "123 Main St", "Anytown", "CA", "12345", "555-1234", 1001, true);
    cout << "Constructor test complete.\n" << endl;

    // Test all accessors
    cout << "Testing accessors..." << endl;
    cout << "Last Name: " << s.getLastName() << endl;
    cout << "First Name: " << s.getFirstName() << endl;
    cout << "Address: " << s.getAddress() << endl;
    cout << "City: " << s.getCity() << endl;
    cout << "State: " << s.getState() << endl;
    cout << "Zip: " << s.getZip() << endl;
    cout << "Phone: " << s.getPhone() << endl;
    cout << "Student ID: " << s.getStudentID() << endl;
    cout << "Incoming Freshman: " << (s.getIncomingFreshman() ? "true" : "false") << endl;
    cout << "Accessor tests complete.\n" << endl;

    // Test all mutators
    cout << "Testing mutators..." << endl;
    s.setLastName("Smith");
    s.setFirstName("Jane");
    s.setAddress("456 Oak Ave");
    s.setCity("Albany");
    s.setState("NY");
    s.setZip("67890");
    s.setPhone("555-6789");
    s.setStudentID(2002);
    s.setIncomingFreshman(false);
    cout << "Mutator tests complete.\n" << endl;

    // Show results after mutators
    cout << "Testing accessors after mutators..." << endl;
    cout << "Last Name: " << s.getLastName() << endl;
    cout << "First Name: " << s.getFirstName() << endl;
    cout << "Address: " << s.getAddress() << endl;
    cout << "City: " << s.getCity() << endl;
    cout << "State: " << s.getState() << endl;
    cout << "Zip: " << s.getZip() << endl;
    cout << "Phone: " << s.getPhone() << endl;
    cout << "Student ID: " << s.getStudentID() << endl;
    cout << "Incoming Freshman: " << (s.getIncomingFreshman() ? "true" : "false") << endl;
    cout << "All tests complete." << endl;
    return 0;
}