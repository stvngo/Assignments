#include "PersonData.h"

PersonData::PersonData(string l, string f, string a, string c, string s, string z, string p) {
    lastName = l;
    firstName = f;
    address = a;
    city = c;
    state = s;
    zip = z;
    phone = p;
}

// Accessors
string PersonData::getLastName() const { return lastName; }
string PersonData::getFirstName() const { return firstName; }
string PersonData::getAddress() const { return address; }
string PersonData::getCity() const { return city; }
string PersonData::getState() const { return state; }
string PersonData::getZip() const { return zip; }
string PersonData::getPhone() const { return phone; }

// Mutators
void PersonData::setLastName(string l) { lastName = l; }
void PersonData::setFirstName(string f) { firstName = f; }
void PersonData::setAddress(string a) { address = a; }
void PersonData::setCity(string c) { city = c; }
void PersonData::setState(string s) { state = s; }
void PersonData::setZip(string z) { zip = z; }
void PersonData::setPhone(string p) { phone = p; }