"""
Guitars! program, practical 6
"""
VINTAGE_YEAR = 50
CURRENT_YEAR = 2021


class Guitar:
    """Represent information about a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage based on age."""
        return self.get_age() > VINTAGE_YEAR
