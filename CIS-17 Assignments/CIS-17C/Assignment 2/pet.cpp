#include "pet.h"
using namespace std;

// Initialize the state of the pet
Pet::Pet(string nm, int initialHealth) {
  m_name = nm;
  m_health = initialHealth;
}

void Pet::eat(int amt) {
  m_health += amt;
}

void Pet::play() {
  if (m_health > 0) {
    m_health -= 1;
  } 
}

string Pet::name() const {
  return m_name; 
}

int Pet::health() const {
  return m_health; 
}

bool Pet::alive() const {
  if (m_health > 0) {
    return true;
  } else
    return false;
}