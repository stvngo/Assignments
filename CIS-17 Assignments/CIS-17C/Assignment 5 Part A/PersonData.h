#ifndef PERSONDATA_H
#define PERSONDATA_H

#include <string>
using namespace std;

class PersonData {
private:
    string lastName;
    string firstName;
    string address;
    string city;
    string state;
    string zip;
    string phone;
public:
    PersonData(string l, string f, string a, string c, string s, string z, string p);
    // Accessors
    string getLastName() const;
    string getFirstName() const;
    string getAddress() const;
    string getCity() const;
    string getState() const;
    string getZip() const;
    string getPhone() const;
    // Mutators
    void setLastName(string l);
    void setFirstName(string f);
    void setAddress(string a);
    void setCity(string c);
    void setState(string s);
    void setZip(string z);
    void setPhone(string p);
};

#endif // PERSONDATA_H