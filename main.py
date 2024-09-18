from customer import Customer
from reservation import Reservation


def main():
    """ creates some objects and calls some methods """

    reservation = Reservation('123', 'ESAF')
    customer = Customer('Julian', reservation)
    print(customer)
    print(reservation)


if __name__ == '__main__':
    main()
