from guitar import Guitar

def main():
    """ A program that fetches other information from CSV files,
    sorts it in year order, and adds and stores new information"""

    filename = "guitars.csv"

    guitars = read_guitars(filename)
    print("Guitar information read from the file:")
    display_guitars(guitars)

    guitars.sort(key=lambda guitar: guitar.year)
    print("\n Guitar information sorted by year (old):")
    display_guitars(guitars)

    new_guitars = get_new_guitars()
    if new_guitars:
        guitars.extend(new_guitars)

    write_guitars(filename, guitars)
    print(f"\n Updated guitar information has been saved in file {filename}.")

def read_guitars(filename):
    """This function reads guitar information from a CSV file and returns a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 3:
                    name = parts[0].strip()
                    try:
                        year = int(parts[1].strip())
                        cost = float(parts[2].strip())
                    except ValueError:
                        print(f"Invalid data type: {line}")
                        continue
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return guitars

def display_guitars(guitars):
    """Prints all the guitar information stored in the list."""
    if not guitars:
        print("There is no other information.")
        return
    for guitar in guitars:
        print(guitar)

def get_new_guitars():
    """This function receives new guitar information from the user and returns a list of Guitar objects."""
    new_guitars = []
    print("Enter new guitar information (leave the name blank to exit):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year_str = input("Year: ").strip()
        cost_str = input("Cost: ").strip()
        try:
            year = int(year_str)
            cost = float(cost_str)
        except ValueError:
            print("The year or cost you entered is invalid. Please try again.")
            continue
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars

def write_guitars(filename, guitars):
    """Log the Guitar object list to the CSV file."""
    try:
        with open(filename, "w") as file:
            for guitar in guitars:
                file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    except Exception as e:
        print("Error writing file:", e)

if __name__ == "__main__":
    main()