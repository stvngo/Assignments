#include "Car.h"
#include <string>
using namespace std;

Car::Car(int year, string make) {
    this->year = year;
    this->make = make;
    this->speed = 0;
}

int Car::getYear() const {
    return year;
}

string Car::getMake() const {
    return make;
}

int Car::getSpeed() const {
    return speed;
}

void Car::accelerate() {
    speed += 5;
}

void Car::brake() {
    speed -= 5;
    if (speed < 0) {
        speed = 0;
    }
}