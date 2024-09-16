import pytest

from customer import Customer
from reservation import Reservation


@pytest.fixture
def reservation():
    return Reservation('123', 'ESAF')


@pytest.fixture
def customer(reservation):
    return Customer('Julian', reservation)


# Test Customer-Objekt und Customer-Referenz in Reservation-Objekt
def test_customer_name(customer):
    assert customer.name == 'Julian'


def test_customers_reservation(customer, reservation):
    assert customer.reservation is reservation


def test_reservation_from_customer(customer, reservation):
    assert reservation.customer is None
