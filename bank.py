class Client:

    def __init__(self, first_name, last_name, pronouns, date_of_birth, occupation, account_balance
                 , overdraft_limit):
        self.first_name = first_name
        self.last_name = last_name
        self.pronouns = pronouns
        self.date_of_birth = date_of_birth
        self.occupation = occupation
        self.account_balance = account_balance
        self.overdraft_limit = overdraft_limit

    def show_details(self):
        print('First name: ', self.first_name)
        print('Last name: ', self.last_name)
        print('pronouns: ', self.pronouns)
        print('date_of_birth: ', self.date_of_birth)
        print('occupation: ', self.occupation)
        print('account_balance: ', self.account_balance)
        print('overdraft_limit: ', self.overdraft_limit)

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance - amount >= -self.overdraft_limit:
            self.account_balance -= amount
        else:
            self.account_balance -= (amount + 5)
