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
client.file_to_list_object()


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
        client.Client(7, 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)  # should raise a TypeError
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


def test_list_by_first_name():
    print(bank.list_by_first_name('John'))


def test_list_by_last_name():
    print(bank.list_by_last_name('Suter'))


def test_list_by_date_of_birth():
    print(bank.list_by_birthday(date(2002, 12, 31)))


def test_list_by_negative_balance():
    print(bank.list_by_negative_balance())


def test_list_all():
    bank.list_all()


def test_delete_client():
    bank.list_all()
    bank.delete_client(john_king)
    bank.list_all()


def test_retrieval():
    print("Client?", isinstance(client.file_to_list_object()[0], client.Client))
    print("Repr:",
          client.file_to_list_object()[0].__repr__() == "Client(Mr, John, King, He/Him, 2002-12-31, Student, 1000, 100)")
    print("Title:", client.file_to_list_object()[0].get_title() == 'Mr')
    print("First name:", client.file_to_list_object()[0].get_first_name() == 'John')
    print("Last name:", client.file_to_list_object()[0].get_last_name() == 'King')
    print("Pronouns:", client.file_to_list_object()[0].get_pronouns() == 'He/Him')
    print("Date of birth:", client.file_to_list_object()[0].get_date_of_birth() == date(2002, 12, 31))
    print("Occupation:", client.file_to_list_object()[0].get_occupation() == 'Student')
    print("Account balance:", client.file_to_list_object()[0].get_account_balance() == 1000)
    print("Overdraft limit:", client.file_to_list_object()[0].get_overdraft_limit() == 100)


def main():
    # test_file_to_list_object()
    test_client()
    test_bad_client()
    test_deposit()
    test_bad_deposit()
    test_withdraw()
    test_withdraw_over_overdraft_limit()
    test_bad_withdraw()
    test_retrieval()
    test_list_by_first_name()


if __name__ == "__main__":
    main()

# def test_client():
#     """This test checks if john is of type Client. Then checks the functions by printing if the
#     instances of john by using the functions are the same as the Client john."""
#
#     print("Client?", isinstance(client.file_to_list_object()[0], client.Client))
#     print("Repr:", client.file_to_list_object()[0].__repr__() == "Client(Mr, John, King, He/Him, 2002-12-31, Student, "
#                                                                  "1000, 100)")
#     print("Title:", client.file_to_list_object()[0].get_title() == 'Mr')
#     print("First name:", client.file_to_list_object()[0].get_first_name() == 'John')
#     print("Last name:", client.file_to_list_object()[0].get_last_name() == 'King')
#     print("Pronouns:", client.file_to_list_object()[0].get_pronouns() == 'He/Him')
#     print("Date of birth:", client.file_to_list_object()[0].get_date_of_birth() == date(2002, 12, 31))
#     print("Occupation:", client.file_to_list_object()[0].get_occupation() == 'Student')
#     print("Account balance:", client.file_to_list_object()[0].get_account_balance() == 1000)
#     print("Overdraft limit:", client.file_to_list_object()[0].get_overdraft_limit() == 100)
#
#
# def test_bad_client():
#     """
#     This is a test for a bad client. This is an example to show that putting a wrong type of value
#     in Client will give a TypeError.
#     """
#
#     try:
#         client.Client(7, 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)  # should raise a TypeError
#     except TypeError:
#         print("Fails as expected")
#     else:
#         print("Should have failed")
#
#
# def test_deposit():
#     client.file_to_list_object()[0].deposit(50)
#     print("Account balance:", client.file_to_list_object()[0].get_account_balance() == 1050)
#
#
# def test_bad_deposit():
#     try:
#         client.file_to_list_object()[0].deposit('20')  # should raise a TypeError
#     except TypeError:
#         print("Fails as expected")
#     else:
#         print("Should have failed")
#
#
# def test_withdraw():
#     client.file_to_list_object()[0].withdraw(50)
#     print("Account balance:", client.file_to_list_object()[0].get_account_balance() == 1000)
#
#
# def test_withdraw_over_overdraft_limit():
#     client.file_to_list_object()[0].withdraw(1101)
#     print("Account balance:", client.file_to_list_object()[0].get_account_balance() == -106)
#
#
# def test_bad_withdraw():
#     try:
#         client.file_to_list_object()[0].withdraw('20')  # should raise a TypeError
#     except TypeError:
#         print("Fails as expected")
#     else:
#         print("Should have failed")
#
#
# def test_set_title():
#     client.file_to_list_object()[0].set_title('Dr')
#     print("Title:", client.file_to_list_object()[0].get_title() == 'Dr')
#
#
# def test_bad_set_title():
#     try:
#         client.file_to_list_object()[0].set_title(50)  # should raise TypeError
#     except TypeError:
#         print("Fails as expected")
#     else:
#         print("Should have failed")
#
#
# def test_set_first_name():
#     client.file_to_list_object()[0].set_first_name('Jon')
#     print("First name:", client.file_to_list_object()[0].get_title() == 'Jon')
#
#
# def test_bad_set_first_name():
#     try:
#         client.file_to_list_object()[0].set_title(50)  # should raise TypeError
#     except TypeError:
#         print("Fails as expected")
#     else:
#         print("Should have failed")
#
# def main():
#     # test_file_to_list_object()
#     test_client()
#     test_bad_client()
#     test_deposit()
#     test_bad_deposit()
#     test_withdraw()
#     test_withdraw_over_overdraft_limit()
#     test_bad_withdraw()
#
#
# if __name__ == "__main__":
#     main()
