'''
FILENAME = "subject_data.txt"

function main
    subjects = load_data()
    display_subjects(subjects)

function load_data
    """Read data from file and return it as a list of lists."""
    subjects = []
    with open(FILENAME, 'r') as input_file
        for line in input_file
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects

function display_subjects(subjects)
    """Print formatted subject details."""
    for subject in subjects
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students.")

main()
'''
FILENAME = "subject_data.txt"

def main():
    subjects = load_data()
    display_subjects(subjects)

def load_data():
    """Read data from file and return it as a list of lists."""
    subjects = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects

def display_subjects(subjects):
    """Print formatted subject details."""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students.")

main()