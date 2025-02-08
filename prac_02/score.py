"""
import random
function main
    score = float(input("Enter score: "))
    result = determine_result(score)
    display "Result:", result

    random_score = random.randint(0, 100)
    display "Random score:", random_score
    display "Result:", determine_result(random_score)

function determine_result(score)
    if score < 0 or score > 100
        return Invalid score
    else if score > 90
        return Excellent
    else if score > 50
        return Passable
    else
        return Bad

main()
"""
import random
def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print("Result:", result)

    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print("Result:", determine_result(random_score))

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

main()