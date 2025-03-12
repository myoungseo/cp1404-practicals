"""
import guitar class

    function __init__(self, name="", year=0, cost=0)
        self.name = name
        self.year = year
        self.cost = cost

    function __str__(self)
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    function get_age(self)
        current_year = 2024
        return current_year - self.year

    function is_vintage(self)
        return self.get_age() >= 50
"""
class Guitar:
    """Represents a Guitar with a name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, otherwise False."""
        return self.get_age() >= 50