from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0

    display_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        display_menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def display_menu():
    """ Display the menu options to the user."""
    print("q)uit, c)hoose taxi, d)rive")

def choose_taxi(taxis):
    """Show available taxis and let the user select one."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None

def drive_taxi(current_taxi):
    """Drive the currently selected taxi a user-specified distance."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    else:
        try:
            distance = float(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            return trip_cost
        except ValueError:
            print("Invalid distance")
            return 0

if __name__ == '__main__':
    main()
