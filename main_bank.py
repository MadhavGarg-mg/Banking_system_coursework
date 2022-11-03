import datetime
import bank


def main():
    john = bank.Client('Mr', 'John', 'King', 'He/Him', datetime.date(2002, 12, 31), 'Student', 1000, 100)
    gare = bank.Client('Mr', 'Gare', 'Coffelt', 'He/Him', datetime.date(2006, 5, 24), 'Student', 25463, 100)
    ab = bank.Client('Mrs', 'Ab', 'Suter', 'She/Her', datetime.date(1986, 5, 26), 'Marketing Assistant', 58670, 100)
    print(john)
    del john


main()
