class Client:

    def __init__(self, title: str, first_name: str, last_name: str, pronouns: str, date_of_birth: str, occupation: str,
                 account_balance: (float, int), overdraft_limit: (float, int)):
        if not isinstance(title, str):
            raise TypeError("Title should be of type string.")
        self.title = title

        if not isinstance(first_name, str):
            raise TypeError("First name should be of type string.")
        self.first_name = first_name

        if not isinstance(last_name, str):
            raise TypeError("Last name should be of type string.")
        self.last_name = last_name

        if not isinstance(pronouns, str):
            raise TypeError("pronouns should be of type string.")
        self.pronouns = pronouns

        if not isinstance(date_of_birth, str):
            raise TypeError("Date of birth should be of type string.")
        self.__date_of_birth = date_of_birth

        if not isinstance(occupation, str):
            raise TypeError("Occupation should be of type string.")
        self.occupation = occupation

        if not isinstance(account_balance, (float, int)):
            raise TypeError("Account balance should be of type integer or float.")
        self.__account_balance = account_balance

        if not isinstance(overdraft_limit, (float, int)):
            raise TypeError("Overdraft limit should be of type integer or float.")
        self.__overdraft_limit = overdraft_limit

    def __repr__(self):
        return f' Client({self.title}, {self.first_name}, {self.last_name}, {self.pronouns},' \
               f' {self.__date_of_birth}, {self.occupation}, {self.__account_balance}, {self.__overdraft_limit})'

    def get_title(self):
        return self.title

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_pronouns(self):
        return self.pronouns

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_occupation(self):
        return self.occupation

    def get_account_balance(self):
        return self.__account_balance

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance - amount >= -self.__overdraft_limit:
            self.__account_balance -= amount
        else:
            self.__account_balance -= (amount + 5)

    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title should be of type string.")
        self.title = title

    def set_first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("First name should be of type string.")
        self.first_name = first_name

    def set_last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError("Last name should be of type string.")
        self.last_name = last_name

    def set_pronouns(self, pronouns):
        if not isinstance(pronouns, str):
            raise TypeError("pronouns should be of type string.")
        self.pronouns = pronouns

    def set_date_of_birth(self, date_of_birth):
        if not isinstance(date_of_birth, str):
            raise TypeError("Date of birth should be of type string.")
        self.__date_of_birth = date_of_birth

    def set_occupation(self, occupation):
        if not isinstance(occupation, str):
            raise TypeError("Occupation should be of type string.")
        self.occupation = occupation

    def set_account_balance(self, account_balance):
        if not isinstance(account_balance, (float, int)):
            raise TypeError("Account balance should be of type integer or float.")
        self.__account_balance = account_balance

    def set_overdraft_limit(self, overdraft_limit):
        if not isinstance(overdraft_limit, (float, int)):
            raise TypeError("Overdraft limit should be of type integer or float.")
        self.__overdraft_limit = overdraft_limit

