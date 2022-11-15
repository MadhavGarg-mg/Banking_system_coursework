from Bank import Bank
import Client
from datetime import date


def main():
    bank = Bank()
    john = Client.Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)
    gare = Client.Client('Mr', 'Gare', 'Coffelt', 'He/Him', date(2006, 5, 24), 'Student', 25463, 100)
    ab = Client.Client('Mrs', 'Ab', 'Suter', 'She/Her', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)
    john1 = Client.Client('Mrs', 'John', 'Suter', 'She/Her', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)

    print(bank.list_by_first_name('john'))
    print(Client.file_to_list_object())
    print(Client.file_to_list_object()[0].get_first_name())
    del john
    print(bank.list_by_first_name('john'))


main()
