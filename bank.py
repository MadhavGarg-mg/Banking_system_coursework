class Client:

    def __init__(self, first_name, last_name, pronouns, date_of_birth, occupation, account_balance, overdraft_limit):
        self.first_name = first_name
        self.last_name = last_name
        self.pronouns = pronouns
        self.date_of_birth = date_of_birth
        self.occupation = occupation
        self.account_balance = account_balance
        self.overdraft_limit = overdraft_limit

    def show_details(self):
        print('Client Details')
        print('First name: ', self.first_name)
        print('Last name: ', self.last_name)
        print('pronouns: ', self.pronouns)
        print('date_of_birth: ', self.date_of_birth)
        print('occupation: ', self.occupation)
        print('account_balance: ', self.account_balance)
        print('overdraft_limit:', self.overdraft_limit)
        return '\r'

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance - amount >= -self.overdraft_limit:
            self.account_balance -= amount
        else:
            self.account_balance -= (amount + 5)

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_pronouns(self, new_pronouns):
        self.pronouns = new_pronouns

    def update_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

    def update_occupation(self, new_occupation):
        self.date_of_birth = new_occupation

    def update_account_balance(self, new_account_balance):
        self.date_of_birth = new_account_balance

    def update_overdraft_limit(self, new_overdraft_limit):
        self.date_of_birth = new_overdraft_limit
