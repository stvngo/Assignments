#include <iostream>
#include "Doctor.h"
#include "Lawyer.h"
#include "SoftwareEngineer.h"
#include "Sales.h"
using namespace std;

// Polymorphic function
void printSalary(const Worker& w) {
    cout << w.getName() << " earns $" << w.getSalary() << " per year, or $" << w.salaryPerWeek() << " per week." << endl;
}

int main() {
    Doctor doc("Dr. Smith");
    Lawyer law("Atty. Jones");
    SoftwareEngineer se("Eng. Lee");
    Sales sales("Ms. Brown");

    cout << "Testing Doctor class..." << endl;
    cout << "Name: " << doc.getName() << endl;
    cout << "Salary: $" << doc.getSalary() << endl;
    printSalary(doc);
    doc.setName("Dr. Adams");
    doc.setSalary(300000.0);
    cout << "After mutators - Name: " << doc.getName() << ", Salary: $" << doc.getSalary() << endl;
    cout << "Salary per week: $" << doc.salaryPerWeek() << endl;
    printSalary(doc);
    cout << endl;

    cout << "Testing Lawyer class..." << endl;
    cout << "Name: " << law.getName() << endl;
    cout << "Salary: $" << law.getSalary() << endl;
    printSalary(law);
    law.setName("Atty. Smith");
    law.setSalary(150000.0);
    cout << "After mutators - Name: " << law.getName() << ", Salary: $" << law.getSalary() << endl;
    cout << "Salary per week: $" << law.salaryPerWeek() << endl;
    printSalary(law);
    cout << endl;

    cout << "Testing SoftwareEngineer class..." << endl;
    cout << "Name: " << se.getName() << endl;
    cout << "Salary: $" << se.getSalary() << endl;
    printSalary(se);
    se.setName("Eng. Kim");
    se.setSalary(120000.0);
    cout << "After mutators - Name: " << se.getName() << ", Salary: $" << se.getSalary() << endl;
    cout << "Salary per week: $" << se.salaryPerWeek() << endl;
    printSalary(se);
    cout << endl;

    cout << "Testing Sales class..." << endl;
    cout << "Name: " << sales.getName() << endl;
    cout << "Salary: $" << sales.getSalary() << endl;
    printSalary(sales);
    sales.setName("Ms. Green");
    sales.setSalary(70000.0);
    cout << "After mutators - Name: " << sales.getName() << ", Salary: $" << sales.getSalary() << endl;
    cout << "Salary per week: $" << sales.salaryPerWeek() << endl;
    printSalary(sales);
    cout << endl;

    return 0;
}