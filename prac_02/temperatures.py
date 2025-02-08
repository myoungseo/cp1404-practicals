"""
function celsius_to_fahrenheit(celsius)
    '''Convert Celsius to Fahrenheit'''
    return celsius * 9.0 / 5 + 32

function fahrenheit_to_celsius(fahrenheit)
    '''Convert Fahrenheit to Celsius'''
    return 5 / 9 * (fahrenheit - 32)

MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit

display menu
get choice
while choice != "Q"
    if choice == "C"
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        display "Result:" {fahrenheit:.2f} "F"
    else if choice == "F"
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        display "Result:" {celsius:.2f} "C"
    else
        display invalid message
    display menu
    get choice

display Thank you message
"""
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")