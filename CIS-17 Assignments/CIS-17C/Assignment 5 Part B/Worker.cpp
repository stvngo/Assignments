#include "Worker.h"

Worker::Worker(string n, double s) {
    name = n;
    salary = s;
}

string Worker::getName() const { return name; }
double Worker::getSalary() const { return salary; }
void Worker::setName(string n) { name = n; }
void Worker::setSalary(double s) { salary = s; } 