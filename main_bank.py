import bank

def main():
    madhav = bank.Client('Madhav', 'Garg', 'He/Him', '11/01/2003', 'Student', 1000, 100)
    madhav.withdraw(1110)
    print(madhav.show_details())

main()
