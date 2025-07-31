#ifndef WORKER_H
#define WORKER_H

#include <string>
using namespace std;

class Worker {
protected:
    string name;
    double salary;
public:
    Worker(string n, double s);
    virtual ~Worker() {}
    string getName() const;
    double getSalary() const;
    void setName(string n);
    void setSalary(double s);
    virtual double salaryPerWeek() const = 0; // pure virtual
};

#endif // WORKER_H 