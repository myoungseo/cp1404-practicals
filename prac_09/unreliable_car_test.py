from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("Sketchy", 100, 30)

total_driven = 0
attempts = 100

print(f"Testing {my_unreliable_car.name} with reliability {my_unreliable_car.reliability}%")

for i in range(attempts):
    driven = my_unreliable_car.drive(1)
    total_driven += driven

print(f"Attempted to drive {attempts} times.")
print(f"Actually drove {total_driven} km.")