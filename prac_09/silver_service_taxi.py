from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
    
    def get_fare(self):
        """Calculate the total fare for the current trip, including flagfall."""
        return super().get_fare() + self.flagfall
    
    def __str__(self):
        """ Return a string representation of the SilverServiceTaxi, including the flagfall information."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"