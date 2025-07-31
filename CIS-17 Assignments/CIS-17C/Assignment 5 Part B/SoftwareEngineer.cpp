#include "SoftwareEngineer.h"

SoftwareEngineer::SoftwareEngineer(string n) : Worker(n, 108080.0) {}

double SoftwareEngineer::salaryPerWeek() const {
    return salary / 52.0;
} 