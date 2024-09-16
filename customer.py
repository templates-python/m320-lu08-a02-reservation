class Customer:
    """
    The customer who makes a reservation for an event

    Attributes
    ----------
    name: String
        the full name of the customer
    reservation: Reservation
        the reservation object for this customer
    """

    def __init__(self, name, reservation):
        """ creates the customer """
        self._name = name
        self._reservation = reservation
        reservation.customer = self

    def __str__(self):
        """ returns as String representation of this customer """
        return f'{self.name} hat eine Reservation für den Anlass {self._reservation.event}'

    @property
    def name(self):
        """ gets the name """
        return self._name

    @property
    def reservation(self):
        """ gets the reservation """
        return self._reservation
