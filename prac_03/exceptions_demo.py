"""
1. When will a ValueError occur?
A ValueError occurs when a non-numeric value is entered during the int(input(...)) conversion process.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the denominator is 0 in the division operation fraction = numerator / denominator.
In other words, an error occurs if the user enters 0 for the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, checking whether the denominator is 0 before performing the division can prevent a ZeroDivisionError.
While loop can be used to repeatedly prompt the user until they enter a non-zero value.

try
    get numerator
    get denominator

    while denominator == 0
        print("Cannot divide by zero! Please enter a valid denominator.")
        get denominator
    fraction = numerator / denominator
    print(fraction)

except ValueError
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero! Please enter a valid denominator.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")