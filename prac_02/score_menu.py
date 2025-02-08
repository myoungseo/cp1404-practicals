'''
MENU = """(G)Get valid score
    (P)Print result
    (S)Show stars
    (Q)uit"""
function main()
    score = get_valid_score()
    display menu
    get choice
    while choice != "Q"
        if choice == "G"
            score = get_valid_score()
        else if choice == "P"
            result = determine_result(score)
            display "Result:", result
        else if choice == "S"
            stars = show_stars(score)
            display stars
        else
            display invalid message
        display menu
        get choice
    display farewell message

function get_valid_score()
    get score
    if score < 0 or score > 100
        display invalid message
        get score
    return score

function determine_result(score)
    if score > 90
        return "Excellent"
    else if score > 50
        return "Passable"
    else
        return "Bad"

function show_stars(score)
    display "*" * score

main()
'''
MENU = """(G)Get valid score
    (P)Print result
    (S)Show stars
    (Q)uit"""
def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print("Result:", result)
        elif choice == "S":
            stars = show_stars(score)
            print(stars)
        else:
            print("Invalid choice. Please enter G, P, S, or Q.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")

def get_valid_score():
    score = int(input("Enter score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
        score = int(input("Enter score (0-100): "))
    return score

def determine_result(score):
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * score)

main()