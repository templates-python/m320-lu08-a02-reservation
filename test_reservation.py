import pytest

from reservation import Reservation


@pytest.fixture
def reservation(self):
    return Reservation('123', 'ESAF')


# Test für Reservation-Objekt. Noch ohne Zuweisung eines Customer-Objekts
def test_reservation_number(reservation):
    assert reservation.number == '123'


def test_reservation_event(reservation):
    assert reservation.event == 'ESAF'


def test_reservation_without_customer(reservation):
    assert reservation.customer == None
