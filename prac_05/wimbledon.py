"""
import csv

function main
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_counts = count_champions(data)
    countries = get_winning_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champion_counts.items():
        print(f"{champion} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

function read_wimbledon_data(filename)
    with open(filename, "r", encoding="utf-8-sig") as file
        reader = csv.reader(file)
        next(reader)
        return list(reader)

function count_champions(data)
    champion_counts = {}
    for row in data
        champion = row[2]
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts

function get_winning_countries(data)
    countries = {row[1] for row in data}
    return sorted(countries)

main()
"""
import csv

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_counts = count_champions(data)
    countries = get_winning_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champion_counts.items():
        print(f"{champion} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def count_champions(data):
    champion_counts = {}
    for row in data:
        champion = row[2]
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts

def get_winning_countries(data):
    countries = {row[1] for row in data}
    return sorted(countries)

main()