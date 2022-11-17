"""This file contains all the tests."""

import client
from bank import Bank
from datetime import date


john_king = client.Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)
gare_coffelt = client.Client('Mr', 'Gare', 'Coffelt', 'He/Him', date(2006, 5, 24), 'Student', 25463, 100)
ab_suter = client.Client('Mrs', 'Ab', 'Suter', 'She/Her', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)
john_suter = client.Client('Dr', 'John', 'Suter', 'He/Him', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)

bank = Bank()
# bank.object_to_file()
print(client.file_to_list_object())

def test_client():
    """This test checks if john is of type Client. Then checks the functions by printing if the
    instances of john by using the functions are the same as the Client john."""

    print("Client?", isinstance(john_king, client.Client))
    print("Repr:",
          john_king.__repr__() == "Client(Mr, John, King, He/Him, 2002-12-31, Student, 1000, 100)")
    print("Title:", john_king.get_title() == 'Mr')
    print("First name:", john_king.get_first_name() == 'John')
    print("Last name:", john_king.get_last_name() == 'King')
    print("Pronouns:", john_king.get_pronouns() == 'He/Him')
    print("Date of birth:", john_king.get_date_of_birth() == date(2002, 12, 31))
    print("Occupation:", john_king.get_occupation() == 'Student')
    print("Account balance:", john_king.get_account_balance() == 1000)
    print("Overdraft limit:", john_king.get_overdraft_limit() == 100)


def test_bad_client():
    """
    This is a test for a bad client. This is an example to show that putting a wrong type of value
    in Client will give a TypeError.
    """

    try:
        client.Client(7, 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000,
               100)  # should raise a TypeError
    except TypeError:
        print("Fails as expected")
    else:
        print("Should have failed")


def test_deposit():
    john_king.deposit(50)
    print("Account balance:", john_king.get_account_balance() == 1050)


def test_bad_deposit():
    try:
        john_king.deposit('20')  # should raise a TypeError
    except TypeError:
        print("Fails as expected")
    else:
        print("Should have failed")


def test_withdraw():
    john_king.withdraw(50)
    print("Account balance:", john_king.get_account_balance() == 1000)


def test_withdraw_over_overdraft_limit():
    john_king.withdraw(1101)
    print("Account balance:", john_king.get_account_balance() == -106)


def test_bad_withdraw():
    try:
        john_king.withdraw('20')  # should raise a TypeError
    except TypeError:
        print("Fails as expected")
    else:
        print("Should have failed")

def test_set_title():
    john_king.set_title('Dr')
    print("Title:", john_king.get_title() == 'Dr')


def test_bad_set_first():
    try:
        john_king.set_title(50)  # should raise TypeError
    except TypeError:
        print("Fails as expected")
    else:
        print("Should have failed")






def main():
    test_file_to_list_object()
    test_client()
    test_bad_client()
    test_deposit()
    test_bad_deposit()
    test_withdraw()
    test_withdraw_over_overdraft_limit()
    test_bad_withdraw()


if __name__ == "__main__":
    main()
