from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 2)

taxi.start_fare()
taxi.drive(18)
fare = taxi.get_fare()

print(f"Fare: ${fare:.2f}")
assert abs(fare - 48.78) < 0.01