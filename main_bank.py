import bank


def main():
    john = bank.Client('Mr', 'John', 'King', 'He/Him', '01/01/2000', 'Student', 1000, 100)
    gare = bank.Client('Mr', 'Gare', 'Coffelt', 'He/Him', '24/05/2006', 'Student', 25463, 100)
    ab = bank.Client('Mrs', 'Ab', 'Suter', 'She/Her', '26/05/1986', 'Marketing Assistant', 58670, 100)
    print(john)
    del john


main()
