# from Client import Client
from datetime import date
import csv


class Bank:
    clients = []

    def __init__(self):
        pass

    def list_by_first_name(self, first_name):
        for i in range(len(self.clients)):
            if self.clients[i][1] == first_name:
                print(Bank.clients[i])
        return ''

    def list_by_last_name(self, last_name):

        for i in range(len(self.clients)):
            if self.clients[i][2] == last_name:
                print(Bank.clients[i])
        return ''

    def list_by_birthday(self, date_of_birth):
        if not isinstance(date_of_birth, date):
            raise TypeError("Date of birth should be of type date.")

        for i in range(len(self.clients)):
            if self.clients[i][4] == date_of_birth:
                print(Bank.clients[i])
        return ''

    def list_by_negative_balance(self):

        for i in range(len(self.clients)):
            if self.clients[i][6] < 0:
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
                if self.clients[i][j] == client.client[j]:
                    result = True
                else:
                    result = False
                    break
            if result:
                del self.clients[i]

    def object_to_file(self):
        with open('clients.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(self.clients)):
                writer.writerow(self.clients[i]) # Save the value of i so u can go ahead instead of appending the same values
