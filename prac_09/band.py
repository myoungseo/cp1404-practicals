class Band:
    """Represents a band, which has multiple musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        """Convert a list of musicians to a string."""
        musician_strs = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strs})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Print all the members of the band playing."""
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs an instrument!")
