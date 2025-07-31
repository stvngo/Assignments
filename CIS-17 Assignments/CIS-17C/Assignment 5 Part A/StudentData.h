#ifndef STUDENTDATA_H
#define STUDENTDATA_H

#include "PersonData.h"

class StudentData : public PersonData {
private:
    int studentID;
    bool incomingFreshman;
public:
    StudentData(string l, string f, string a, string c, string s, string z, string p, int id, bool freshman);
    // Accessors
    int getStudentID() const;
    bool getIncomingFreshman() const;
    // Mutators
    void setStudentID(int id);
    void setIncomingFreshman(bool freshman);
};

#endif // STUDENTDATA_H 