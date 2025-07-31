#ifndef LAWYER_H
#define LAWYER_H

#include "Worker.h"

class Lawyer : public Worker {
public:
    Lawyer(string n);
    double salaryPerWeek() const override;
};

#endif // LAWYER_H 