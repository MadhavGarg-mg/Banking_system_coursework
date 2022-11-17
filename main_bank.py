from bank import Bank
import client
from datetime import date


def main():
    """
    This is the main for the banking system.
    """
    bank = Bank()
    john_king = client.Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000,
                              100)
    gare_coffelt = client.Client('Mr', 'Gare', 'Coffelt', 'He/Him', date(2006, 5, 24), 'Student',
                                 25463,
                                 100)
    ab_suter = client.Client('Mrs', 'Ab', 'Suter', 'She/Her', date(1986, 5, 26),
                             'Marketing Assistant',
                             58670, 100)
    john_suter = client.Client('Dr', 'John', 'Suter', 'She/Her', date(1986, 5, 26),
                               'Marketing Assistant', 58670, 100)
    bank.object_to_file()
    print(bank.list_all())
    bank.delete_client(john_king)
    print(bank.list_all())

main()
