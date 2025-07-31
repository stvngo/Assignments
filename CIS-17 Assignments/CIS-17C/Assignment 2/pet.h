#ifndef PET_H
#define PET_H

#include <string>
using namespace std;

class Pet { // blueprint for a pet object
  public:
    Pet(string nm, int initialHealth);
    void eat(int amt);
    void play();
    string name() const;
    int health() const;
    bool alive() const;
  private:
    string m_name;
    int m_health;
};

#endif 