# Practical 07
It comprehensively covers object-oriented programming, file input/output, data parsing, user interface design, and fundamental principles of software development (such as Clean Code, SRP, and DRY).

## Author
- Name : Choi Myeongseo
- JCU ID : 14763487
- Github Link : https://github.com/myoungseo/cp1404-practicals

## project_management.py

### Project Data Loading
Reads tab-separated project data from a default file (e.g., projects.txt) or a user-specified file, and creates a Project class instance for each line.

### Project Saving
Saves the in-memory project objects to a file in tab-separated format, using either a default file or a filename specified by the user.

### Project Display
Separates projects into incomplete and complete groups, sorts each group by priority, and prints them.

### Project Filtering
Accepts a date from the user, filters out projects that start after that date, sorts them in chronological order, and prints the results.

### Project Adding and Updating
Creates a new Project object from user input and adds it to the list, while also allowing updates to the completion rate or priority of existing projects.

### Menu System
Provides various options (Load, Save, Display, Filter, Add, Update, Exit) so the user can choose the desired functionality.

## Lessons Learned about Clean Code
- Single Responsibility Principle (SRP) : Design each function and class to perform only one task, enhancing the code's maintainability and scalability.
- DRY (Don't Repeat Yourself) : Minimize duplicate code by modularizing common functionalities into separate functions to ensure consistency and reusability.
- Proper Commenting and Documentation : Clearly explain complex code segments and the roles of functions using comments and docstrings, so that other developers—or your future self—can easily understand and use the code.
