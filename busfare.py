class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self):
        super().__init__(50)

    def fare(self):
        bus_fare = super().fare()
        maintenance_charge = bus_fare * 0.10
        total_fare = bus_fare + maintenance_charge
        return f"Total fare: INR {total_fare}"


bus = Bus()
print(bus.fare())