#ifndef CAR_H
#define CAR_H

#include <string>

class Car {
    private:
        int year;
        std::string make;
        int speed;

    public:
        Car(int year, std::string make);
        int getYear() const;
        std::string getMake() const;
        int getSpeed() const;
        void accelerate();
        void brake();
};

#endif