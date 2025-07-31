#include "StudentData.h"

StudentData::StudentData(string l, string f, string a, string c, string s, string z, string p, int id, bool freshman)
    : PersonData(l, f, a, c, s, z, p) {
    studentID = id;
    incomingFreshman = freshman;
}

// Accessors
int StudentData::getStudentID() const { return studentID; }
bool StudentData::getIncomingFreshman() const { return incomingFreshman; }

// Mutators
void StudentData::setStudentID(int id) { studentID = id; }
void StudentData::setIncomingFreshman(bool freshman) { incomingFreshman = freshman; } 