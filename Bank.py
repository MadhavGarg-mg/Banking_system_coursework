# from Client import Client
from datetime import date


class Bank:
    clients = []

    def __init__(self):
        pass

    def list_by_first_name(self, first_name):
        for i in range(len(self.clients)):
            if Bank.clients[i][1] == first_name:
                print(Bank.clients[i])
        return ''

    def list_by_last_name(self, last_name):

        for i in range(len(self.clients)):
            if Bank.clients[i][2] == last_name:
                print(Bank.clients[i])
        return ''

    def list_by_birthday(self, date_of_birth):
        if not isinstance(date_of_birth, date):
            raise TypeError("Date of birth should be of type date.")

        for i in range(len(self.clients)):
            if Bank.clients[i][4] == date_of_birth:
                print(Bank.clients[i])
        return ''

    def list_by_negative_balance(self):

        for i in range(len(self.clients)):
            if Bank.clients[i][6] < 0:
                print(Bank.clients[i])
        return ''

    def list_all(self):
        for i in range(len(self.clients)):
            print(self.clients[i])
        return ''

    def delete_client(self, client):
        result = None
        for i in range(len(self.clients)):
            for j in range(7):
                if Bank.clients[i][j] == client.clients[j]:
                    result = True
                else:
                    result = False
                    break
            if result:
                del Bank.clients[i]
                del client.clients
                break
