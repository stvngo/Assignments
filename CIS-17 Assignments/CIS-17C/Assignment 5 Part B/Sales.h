#ifndef SALES_H
#define SALES_H

#include "Worker.h"

class Sales : public Worker {
public:
    Sales(string n);
    double salaryPerWeek() const override;
};

#endif // SALES_H 