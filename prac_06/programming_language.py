"""
import class

    function __init__(self, name, typing, reflection, year)
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    function is_dynamic(self)
        return self.typing.lower() == "dynamic"

    function __str__(self)
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
"""

class ProgrammingLanguage:
    """Represents a programming language with typing, reflection, and year of introduction."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language uses dynamic typing, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a formatted string representation of the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"