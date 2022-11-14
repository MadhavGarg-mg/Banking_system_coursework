from datetime import date
from Client import Client
from Bank import Bank

def main():
    bank = Bank()
    john = Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)
    gare = Client('Mr', 'Gare', 'Coffelt', 'He/Him', date(2006, 5, 24), 'Student', 25463, 100)
    ab = Client('Mrs', 'Ab', 'Suter', 'She/Her', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)
    john1 = Client('Mrs', 'John', 'Suter', 'She/Her', date(1986, 5, 26), 'Marketing Assistant', 58670, 100)

    bank.list_by_first_name('John')
    bank.delete_client(john1)
    bank.list_by_first_name('John')
    print(john1)


main()
