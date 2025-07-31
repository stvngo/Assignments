#include "Sales.h"

Sales::Sales(string n) : Worker(n, 64310.0) {}

double Sales::salaryPerWeek() const {
    return salary / 52.0;
} 