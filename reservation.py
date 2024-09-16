class Reservation:
    """
    A reservation for an event

    Attributes
    ----------
    event: String
        the name of the event
    number: String
        the reservation number
    customer: Customer
        the customer this reservation belongs to
    """

    def __init__(self, number, name):
        """ Creates the reservation """
        self._event = name
        self._number = number
        self._the_customer = None

    def __str__(self):
        """ Returns a String representation of this reservation """

        if self.customer is not None:
            return f'Reservation {self.number} {self.event} für Kunde {self.customer.name}'
        else:
            return f'{self.event} ist kein Kunde zugeordnet'

    @property
    def event(self):
        """ gets the event """
        return self._event

    @property
    def number(self):
        """ gets the number """
        return self._number

    @property
    def customer(self):
        """ gets the customer """
        return self._the_customer

    @customer.setter
    def customer(self, customer):
        """ sets the customer """
        self._the_customer = customer


