'''
Time Estimate : 3 hours
'''
from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initializes the Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        """Returns the project information as a formatted string."""
        start_date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_str}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Compares project objects based on their priorities."""
        return self.priority < other.priority

    def is_complete(self):
        """Returns True if the project is complete, otherwise returns False."""
        return self.completion == 100