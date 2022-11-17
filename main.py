"""This file contains all the tests."""

import client
from bank import Bank
from datetime import date

john_king = client.Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)
gare_coffelt = client.Client('Mr', 'Gare', 'Coffelt', 'He/Him', date(2006, 5, 24), 'Student', 0, 0)
ab_suter = client.Client('Mrs', 'Ab', 'Suter', 'She/Her', date(1986, 5, 26), 'Marketing Assistant', 1, 1000)
john_suter = client.Client('Dr', 'John', 'Suter', 'He/Him', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)
minnie_adamo = client.Client('Dr', 'Minnie', 'Adamo', 'He/Him', date(1969, 8, 4), 'Analyst Programmer', -58718, 839)

bank = Bank()


def test_client():
    """This test checks if john is of type Client. Then checks the functions by printing if the
    instances of john by using the functions are the same as the Client john."""
    if isinstance(john_king, client.Client):
        print('test_client: Passed as expected')
    else:
        print('test_client: Should have passed')

    if isinstance(gare_coffelt, client.Client):
        print('test_client: Passed as expected')
    else:
        print('test_client: Should have passed')

    if isinstance(ab_suter, client.Client):
        print('test_client: Passed as expected')
    else:
        print('test_client: Should have passed')

    if john_king.__str__() == 'Mr, John, King, He/Him, 2002-12-31, Student, 1000, 100':
        print('string: Passed as expected')
    else:
        print('string: Should have passed')

    if john_king.__repr__() == "Client(Mr, John, King, He/Him, 2002-12-31, Student, 1000, 100)":
        print('represent: Passed as expected')
    else:
        print('represent: Should have passed')


def test_bad_client():
    """
    This is a test for a bad client. This is an example to show that putting a wrong type of value
    in Client will give a TypeError.
    """
    try:
        client.Client(7, 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)  # should raise a TypeError
    except TypeError:
        print('test_bad_client: Fails as expected')
    else:
        print('test_bad_client: Should have failed')


def test_getters():
    """This test checks all the getter functions."""
    if john_king.get_title() == 'Mr':
        print('getter_title: Passed as expected')
    else:
        print('getter_title: Should have passed')

    if john_king.get_first_name() == 'John':
        print('getter_first_name: Passed as expected')
    else:
        print('getter_first_name: Should have passed')

    if john_king.get_last_name() == 'King':
        print('getter_last_name: Passed as expected')
    else:
        print('getter_last_name: Should have passed')

    if john_king.get_pronouns() == 'He/Him':
        print('getter_pronoun: Passed as expected')
    else:
        print('getter_pronoun: Should have passed')

    if john_king.get_date_of_birth() == date(2002, 12, 31):
        print('getter_date_of_birth: Passed as expected')
    else:
        print('getter_date_of_birth: Should have passed')

    if john_king.get_occupation() == 'Student':
        print('getter_occupation: Passed as expected')
    else:
        print('getter_occupation: Should have passed')

    if john_king.get_account_balance() == 1000:
        print('getter_account_balance: Passed as expected')
    else:
        print('getter_account_balance: Should have passed')

    if john_king.get_overdraft_limit() == 100:
        print('getter_overdraft_limit: Passed as expected')
    else:
        print('getter_overdraft_limit: Should have passed')


def test_deposit():
    """This test checks if we deposit money into a client's account, then the account balance should change
    according to it """
    john_king.deposit(50)
    if john_king.get_account_balance() == 1050:
        print('test_deposit: Passed as expected')
    else:
        print('test_deposit: Should have passed')


def test_bad_deposit_string():
    """This test will fail and give a TypeError as the deposit amount is of type string."""
    try:
        john_king.deposit('20')  # should raise a TypeError
    except TypeError:
        print("test_bad_deposit_string: Fails as expected")
    else:
        print("test_bad_deposit_string: Should have failed")


def test_bad_deposit_negative():
    """This test will fail and give a TypeError as the deposit amount is negative."""
    try:
        john_king.deposit(-50)  # should raise a TypeError
    except TypeError:
        print("test_bad_deposit_negative: Fails as expected")
    else:
        print("test_bad_deposit_negative: Should have failed")


def test_withdraw():
    """This test checks if we withdraw money from a client's account, then the account balance should change
    according to it """
    john_king.withdraw(50)
    if john_king.get_account_balance() == 1000:
        print('test_withdraw: Passed as expected')
    else:
        print('test_withdraw: Should have passed')


def test_withdraw_over_overdraft_limit():
    """This test checks if we withdraw money from a client's account more than the overdraft limit for the client, and
    if it charges them 5 extra for the transaction."""
    john_king.withdraw(1101)
    if john_king.get_account_balance() == -106:
        print('test_withdraw_over_overdraft_limit: Passed as expected')
    else:
        print('test_withdraw_over_overdraft_limit: Should have passed')


def test_bad_withdraw_string():
    """This test will fail and give a TypeError as the withdrawal amount is of type string."""
    try:
        john_king.withdraw('20')  # should raise a TypeError
    except TypeError:
        print("test_bad_withdraw_string: Fails as expected")
    else:
        print("test_bad_withdraw_string: Should have failed")


def test_bad_withdraw_negative():
    """This test will fail and give a TypeError as the withdrawal amount is negative."""
    try:
        john_king.withdraw(-20)  # should raise a TypeError
    except TypeError:
        print("test_bad_withdraw_negative: Fails as expected")
    else:
        print("test_bad_withdraw_negative: Should have failed")


def test_setters():
    """This test checks all the setter functions."""
    minnie_adamo.set_title('Dr')
    if minnie_adamo.get_title() == 'Dr':
        print('setter_title: Passed as expected')
    else:
        print('setter_title: Should have passed')

    minnie_adamo.set_first_name('Minni')
    if minnie_adamo.get_first_name() == 'Minni':
        print('setter_first_name: Passed as expected')
    else:
        print('setter_first_name: Should have passed')

    minnie_adamo.set_last_name('Adam')
    if minnie_adamo.get_last_name() == 'Adam':
        print('setter_last_name: Passed as expected')
    else:
        print('setter_last_name: Should have passed')

    minnie_adamo.set_pronouns('She/Her')
    if minnie_adamo.get_pronouns() == 'She/Her':
        print('setter_pronouns: Passed as expected')
    else:
        print('setter_pronouns: Should have passed')

    minnie_adamo.set_date_of_birth(date(2000, 1, 1))
    if minnie_adamo.get_date_of_birth() == date(2000, 1, 1):
        print('setter_date_of_birth: Passed as expected')
    else:
        print('setter_date_of_birth: Should have passed')

    minnie_adamo.set_occupation('Student')
    if minnie_adamo.get_occupation() == 'Student':
        print('setter_occupation: Passed as expected')
    else:
        print('setter_occupation: Should have passed')


def test_bad_setters():
    """This test gives a TypeError as the title is not a string."""
    try:
        john_king.set_title(50)  # should raise TypeError
    except TypeError:
        print("test_bad_setters: Fails as expected")
    else:
        print("test_bad_setters: Should have failed")


def test_list_by_first_name():
    """This test checks if the list of all first name John's all have first names John."""
    list_first_name = bank.list_by_first_name('John')
    result = False
    for person in list_first_name:
        if person[1] == 'John':
            result = True
        else:
            result = False
            break
    if result:
        print('test_list_by_first_name: Passed as expected')
    else:
        print('test_list_by_first_name: Should have failed')


def test_list_by_last_name():
    """This test checks if the list of all last name Suter's all have last names Suter."""
    list_last_name = bank.list_by_last_name('Suter')
    result = False
    for person in list_last_name:
        if person[2] == 'Suter':
            result = True
        else:
            result = False
            break
    if result:
        print('test_list_by_last_name: Passed as expected')
    else:
        print('test_list_by_last_name: Should have passed')


def test_list_by_date_of_birth():
    """This test checks if the list of all date of birth (1986, 5, 26) all have date of birth (1986, 5, 26)."""
    list_birthday = bank.list_by_birthday(date(1986, 5, 26))
    result = False
    for person in list_birthday:
        if person[4] == date(1986, 5, 26):
            result = True
        else:
            result = False
            break
    if result:
        print('test_list_by_date_of_birth: Passed as expected')
    else:
        print('test_list_by_date_of_birth: Should have passed')


def test_list_by_negative_balance():
    """This test checks if the list of all negative balance clients all have negative balance clients."""
    list_negative = bank.list_by_negative_balance()
    result = False
    for person in list_negative:
        if person[6] < 0:
            result = True
        else:
            result = False
            break
    if result:
        print('test_list_by_negative_balance: Passed as expected')
    else:
        print('test_list_by_negative_balance: Should have passed')


def test_list_all():
    """This test will print all the clients."""
    print(bank.list_all())


def test_object_to_file():
    """This test will create a file clients.csv, and it will have all the clients in it."""
    bank.object_to_file('clients.csv', 'a')


def test_file_to_list_object():
    """This test will check if the client data from the csv file can be retrieved."""
    print(client.file_to_list_object('test_clients.csv'))  # Can handle more than 100 clients


def test_delete_client():
    """This test check if we can successfully delete a client for the list of all clients."""
    number_client_before = len(bank.list_all())
    bank.delete_client(minnie_adamo)
    number_clients_after = len(bank.list_all())
    if number_client_before == number_clients_after + 1:
        print('test_delete_client: Passed as expected')
    else:
        print('test_delete_client: Should have passed')


def main():
    test_client()
    test_bad_client()
    test_getters()
    test_deposit()
    test_bad_deposit_string()
    test_bad_deposit_negative()
    test_withdraw()
    test_withdraw_over_overdraft_limit()
    test_bad_withdraw_string()
    test_bad_withdraw_negative()
    test_setters()
    test_list_by_first_name()
    test_list_by_last_name()
    test_list_by_date_of_birth()
    test_list_by_negative_balance()
    test_list_all()
    test_object_to_file()
    test_file_to_list_object()
    test_delete_client()


if __name__ == "__main__":
    main()
