import bank


def main():
    madhav = bank.Client('Madhav', 'Garg', 'He/Him', '11/01/2003', 'Student', 1000, 100)
    gare = bank.Client('Gare', 'Coffelt', 'He/Him', '24/05/2006', 'Student', 25463, 100)
    ab = bank.Client('Ab', 'Suter', 'They/Them', '26/05/1986', 'Marketing Assistant', 58670, 100)

    print(gare.show_details())
    print(ab.show_details())
    madhav.update_first_name('Madhav1')
    print(madhav.show_details())


main()
