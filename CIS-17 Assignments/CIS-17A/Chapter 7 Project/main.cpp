#include <iostream>
#include "Car.h"

using namespace std;

int main() {
    Car car(2024, "Toyota");
    car.accelerate();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl; // get the speed of the car
    car.accelerate();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.accelerate();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.accelerate();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.accelerate();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.brake();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.brake();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.brake();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.brake();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    car.brake();
    cout << "The car's speed is " << car.getSpeed() << " mph." << endl;
    cout << "The car's year is " << car.getYear() << endl; // get the year of the car
    cout << "The car's make is " << car.getMake() << endl; // get the make of the car
    return 0;
}