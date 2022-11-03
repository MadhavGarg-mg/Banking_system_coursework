from datetime import date


class Client:
    clients = []

    def __init__(self, title: str, first_name: str, last_name: str, pronouns: str, date_of_birth: date, occupation: str,
                 account_balance: (float, int), overdraft_limit: (float, int)):
        if not isinstance(title, str):
            raise TypeError("Title should be of type string.")
        if not isinstance(first_name, str):
            raise TypeError("First name should be of type string.")
        if not isinstance(last_name, str):
            raise TypeError("Last name should be of type string.")
        if not isinstance(pronouns, str):
            raise TypeError("pronouns should be of type string.")
        if not isinstance(date_of_birth, date):
            raise TypeError("Date of birth should be of type date.")
        if not isinstance(occupation, str):
            raise TypeError("Occupation should be of type string.")
        if not isinstance(account_balance, (float, int)):
            raise TypeError("Account balance should be of type integer or float.")
        if not isinstance(overdraft_limit, (float, int)):
            raise TypeError("Overdraft limit should be of type integer or float.")

        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.pronouns = pronouns
        self.__date_of_birth = date_of_birth
        self.occupation = occupation
        self.__account_balance = account_balance
        self.__overdraft_limit = overdraft_limit
        # self.all = [title, first_name, last_name, pronouns, date_of_birth, occupation, account_balance,
        # overdraft_limit]
        # self.clients.append(self.all)

    def __repr__(self) -> str:
        """This function returns all the information of the Client"""
        return f' Client({self.title}, {self.first_name}, {self.last_name}, {self.pronouns},' \
               f' {self.__date_of_birth}, {self.occupation}, {self.__account_balance}, {self.__overdraft_limit})'

    def get_title(self) -> str:
        """This function returns the title of the Client"""
        return self.title

    def get_first_name(self) -> str:
        """This function returns the first_name of the Client"""
        return self.first_name

    def get_last_name(self) -> str:
        """This function returns the last_name of the Client"""
        return self.last_name

    def get_pronouns(self) -> str:
        """This function returns the pronouns of the Client"""
        return self.pronouns

    def get_date_of_birth(self) -> date:
        """This function returns the date_pf_birth of the Client"""
        return self.__date_of_birth

    def get_occupation(self) -> str:
        """This function returns the occupation of the Client"""
        return self.occupation

    def get_account_balance(self) -> (float, int):
        """This function returns the account_balance of the Client"""
        return self.__account_balance

    def get_overdraft_limit(self) -> (float, int):
        """This function returns the overdraft_limit of the Client"""
        return self.__overdraft_limit

    def deposit(self, amount: float):
        """This function adds the amount in the account_balance of the Client"""
        self.__account_balance += amount

    def withdraw(self, amount):
        """This function subtracts the amount in the account_balance of the Client if the account_balance is above
        the overdraft_limit, otherwise it subtracts 5 extra for every transaction surpassing the overdraft_limit"""
        if self.__account_balance - amount >= -self.__overdraft_limit:
            self.__account_balance -= amount
        else:
            self.__account_balance -= (amount + 5)

    def set_title(self, title: str):
        """This function sets the title of the client"""
        if not isinstance(title, str):
            raise TypeError("Title should be of type string.")
        self.title = title

    def set_first_name(self, first_name: str):
        """This function sets the first_name of the client"""
        if not isinstance(first_name, str):
            raise TypeError("First name should be of type string.")
        self.first_name = first_name

    def set_last_name(self, last_name: str):
        """This function sets the last_name of the client"""
        if not isinstance(last_name, str):
            raise TypeError("Last name should be of type string.")
        self.last_name = last_name

    def set_pronouns(self, pronouns: str):
        """This function sets the pronouns of the client"""
        if not isinstance(pronouns, str):
            raise TypeError("pronouns should be of type string.")
        self.pronouns = pronouns

    def set_date_of_birth(self, date_of_birth: str):
        """This function sets the date_of_birth of the client"""
        if not isinstance(date_of_birth, str):
            raise TypeError("Date of birth should be of type date.")
        self.__date_of_birth = date_of_birth

    def set_occupation(self, occupation: str):
        """This function sets the occupation of the client"""
        if not isinstance(occupation, str):
            raise TypeError("Occupation should be of type string.")
        self.occupation = occupation

    def set_account_balance(self, account_balance: (float, int)):
        """This function sets the account_balance of the client"""
        if not isinstance(account_balance, (float, int)):
            raise TypeError("Account balance should be of type integer or float.")
        self.__account_balance = account_balance

    def set_overdraft_limit(self, overdraft_limit: (float, int)):
        """This function sets the overdraft_limit of the client"""
        if not isinstance(overdraft_limit, (float, int)):
            raise TypeError("Overdraft limit should be of type integer or float.")
        self.__overdraft_limit = overdraft_limit

    def list_all(self):
        lst = [self.title, self.first_name, self.last_name, self.pronouns, self.__date_of_birth, self.occupation,
               self.__account_balance, self.__overdraft_limit]
        self.clients.append(lst)
        for i in range(len(Client.clients)):
            print(*Client.clients[i])
