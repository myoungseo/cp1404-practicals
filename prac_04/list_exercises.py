'''
function main
    numbers = []

    for i in range(5)
        number = int(input(f"Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {find_min(numbers)}")
    print(f"The largest number is {find_max(numbers)}")
    print(f"The average of the numbers is {calculate_average(numbers):.1f}")

function find_min(numbers)
    min_value = numbers[0]
    for number in numbers
        if number < min_value
            min_value = number
    return min_value

function find_max(numbers)
    max_value = numbers[0]
    for number in numbers
        if number > max_value
            max_value = number
    return max_value

function calculate_average(numbers)
    total = 0
    for number in numbers
        total += number
    return total / len(numbers)

main()
'''
def main():
    numbers = []

    for i in range(5):
        number = int(input(f"Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {find_min(numbers)}")
    print(f"The largest number is {find_max(numbers)}")
    print(f"The average of the numbers is {calculate_average(numbers):.1f}")

def find_min(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

main()