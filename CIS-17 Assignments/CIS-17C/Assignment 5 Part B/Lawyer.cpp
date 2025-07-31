#include "Lawyer.h"

Lawyer::Lawyer(string n) : Worker(n, 144230.0) {}

double Lawyer::salaryPerWeek() const {
    return salary / 52.0;
} 