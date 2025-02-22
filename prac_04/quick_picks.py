'''
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_COUNT = 6

function main
    get number of picks
    for _ in range(num_picks)
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

function generate_quick_pick
    numbers = []
    while len(numbers) < NUM_COUNT
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers
            numbers.append(num)
    numbers.sort()
    return numbers

main()
'''
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_COUNT = 6

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))
def generate_quick_pick():
    numbers = []
    while len(numbers) < NUM_COUNT:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    return numbers

main()