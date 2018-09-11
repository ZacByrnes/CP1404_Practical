from taxi import Taxi


class SilverServiceTaxi(Taxi):
    fanciness = 0.0
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().print_string(),
                                                                                      self.current_fare_distance,
                                                                                      self.price_per_km * self.fanciness,
                                                                                      self.flagfall)

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().distance_travelled(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

