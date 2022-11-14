from Client import Client
from Bank import Bank


def main():
    bank = Bank()
    john = Client('Mr', 'John', 'King', 'He/Him', '31, 12, 2002', 'Student', 1000, 100)
    gare = Client('Mr', 'Gare', 'Coffelt', 'He/Him', '24, 5 2006,', 'Student', 25463, 100)
    ab = Client('Mrs', 'Ab', 'Suter', 'She/Her', '26, 5, 1986', 'Marketing Assistant', 58670, 100)
    john1 = Client('Mrs', 'John', 'Suter', 'She/Her', '26, 5, 1986', 'Marketing Assistant', 58670, 100)

    bank.list_all()
    Client.file_to_object()


main()
