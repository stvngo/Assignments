#include "Doctor.h"

Doctor::Doctor(string n) : Worker(n, 294000.0) {}

double Doctor::salaryPerWeek() const {
    return salary / 52.0;
} 