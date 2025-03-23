'''
Time Estimate : 7 hours
'''
from project import Project
from datetime import datetime

def main():
    menu()

def load_projects(filename):
    """ Loads project data from the specified file and returns a list of Project objects. """
    projects = []
    try:
        with open(filename, "r") as file:
            header = file.readline()
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")

                if len(parts) != 5:
                    print(f"Invalid data format: {line}")
                name, start_date, priority, cost_estimate, completion = parts
                try:
                    project = Project(name, start_date, priority, cost_estimate, completion)
                    projects.append(project)
                except Exception as e:
                    print(f"An error occurred while creating the project.: {line} - {e}")
    except FileNotFoundError:
        print(f"File {filename} cannot be found.")
    return projects


def save_projects(filename, projects):
    """Saves the project list to the specified file."""
    try:
        with open(filename, "w") as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
            for project in projects:
                start_date_str = project.start_date.strftime("%d/%m/%Y")
                file.write(
                    f"{project.name}\t{start_date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")
        print(f"Project data has been saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the file.: {e}")


def display_projects(projects):
    """ Divides the project list into incomplete and complete projects, sorts each group by priority,
    and prints the results."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for p in incomplete:
        print("  ", p)
    print("Completed projects:")
    for p in complete:
        print("  ", p)


def filter_projects_by_date(projects):
    """Accepts a date from the user and sorts the projects that start after that date in chronological order."""
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_input, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)


def add_new_project():
    """Receives new project information from the user, creates a Project object, and returns it."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date = input("Start date (dd/mm/yyyy): ").strip()
    priority = input("Priority: ").strip()
    cost_estimate = input("Cost estimate: ").strip()
    completion = input("Percent complete: ").strip()

    try:
        project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
        return project
    except Exception as e:
        print("An error occurred while adding the project.", e)
        return None

def update_project(projects):
    """After printing the project list, select a project to modify and update its completion rate and priority."""
    if not projects:
        print("There are no projects to modify.")
        return
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        if choice < 0 or choice >= len(projects):
            print("Invalid selection")
            return
    except ValueError:
        print("You must enter a number.")
        return

    project = projects[choice]
    print(project)

    new_completion = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()

    if new_completion != "":
        try:
            project.completion = int(new_completion)
        except ValueError:
            print("Please enter a valid completion rate number.")
    if new_priority != "":
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Please enter a valid priority number.")


def menu():
    """Main Function"""
    default_filename = "projects.txt"
    projects = load_projects(default_filename)
    print(f"Loaded {len(projects)} projects from {default_filename}")

    menu_text = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""
    print(menu_text)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load projects from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Enter filename to save projects to: ").strip()
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            new_project = add_new_project()
            if new_project:
                projects.append(new_project)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option, please try again.")
            choice = input(">>> ").strip().lower()
    save_default = input(f"Would you like to save to {default_filename}? ").strip().lower()
    if save_default in ["yes", "y"]:
        save_projects(default_filename, projects)
    print("Thank you for using custom-built project management software.")

if __name__ == "__main__":
    main()