"""
Practical 06, Intermediate Exercises
"""


class ProgrammingLanguage:
    """Represent information for a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a programming language from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
