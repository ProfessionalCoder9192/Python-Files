class Ferrari:
    def fuel_type(self):
        return "Fuel Type: Petrol"

    def max_speed(self):
        return "Max Speed: 340 km/h"


class BMW:
    def fuel_type(self):
        return "Fuel Type: Diesel"

    def max_speed(self):
        return "Max Speed: 250 km/h"


def car_details(car):
    print(car.fuel_type())
    print(car.max_speed())


ferrari = Ferrari()
bmw = BMW()

for car in (ferrari, bmw):
    car_details(car)
