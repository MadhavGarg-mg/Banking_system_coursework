import bank


def main():
    madhav = bank.Client('Mr.', 'Madhav', 'Garg', 'He/Him', ' ', 'Student', 1000, 100)
    gare = bank.Client('Mr.', 'Gare', 'Coffelt', 'He/Him', '24/05/2006', 'Student', 25463, 100)
    ab = bank.Client('Mrs.', 'Ab', 'Suter', 'She/Her', '26/05/1986', 'Marketing Assistant', 58670, 100)
    x = input("what do you want to do?")
    print(gare.show_details())
    print(ab.show_details())
    madhav.update_first_name('Madhav1')
    print(madhav.show_details())


main()
