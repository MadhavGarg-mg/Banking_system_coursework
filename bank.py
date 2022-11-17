from datetime import date
import csv


class Bank:
    """
    This is a class for a bank to find clients and delete clients.
    """
    clients = []

    def __init__(self) -> None:
        """
        The constructor for the Bank class.
        """
        pass

    # def add_client(self, client):
    #     """
    #             This function takes the argument first_name and returns the list of the information of
    #             all clients with that first name.
    #
    #             Attributes:
    #                 client (object): The client.
    #             """
    #     self.clients.append(client)
    #

    def list_by_first_name(self, first_name: str) -> list[list]:
        """
        This function takes the argument first_name and returns the list of the information of
        all clients with that first name.

        Attributes:
            first_name (str): The first name of the client.

        Return:
             first_name_list (list[list]): list with a list of all the information of the clients.
        """
        first_name_list = []
        for i in range(len(self.clients)):
            if self.clients[i][1] == first_name:
                first_name_list.append(Bank.clients[i])
        return first_name_list

    def list_by_last_name(self, last_name: str) -> list[list]:
        """
        This function takes the argument last_name and returns the list of the information of
        all clients with that last name.

        Attributes:
            last_name (str): The first name of the client.

        Return:
            last_name_list (list[list]): list with a list of all the information of the clients.
        """
        last_name_list = []
        for i in range(len(self.clients)):
            if self.clients[i][2] == last_name:
                last_name_list.append(Bank.clients[i])
        return last_name_list

    def list_by_birthday(self, date_of_birth: date) -> list[list]:
        """
        This function takes the argument date_of_birth and returns the list of the information of
        all clients with that date of birth.

        Attributes:
            date_of_birth (date): The date of birth of the client.

        Return:
            date_of_birth_list (list[list]): list with a list of all the information of the clients.
        """
        if not isinstance(date_of_birth, date):
            raise TypeError("Date of birth should be of type date.")

        date_of_birth_list = []
        for i in range(len(self.clients)):
            if self.clients[i][4] == date_of_birth:
                date_of_birth_list.append(Bank.clients[i])
        return date_of_birth_list

    def list_by_negative_balance(self) -> list[list]:
        """
        This function returns the list of the information of all clients with negative balance.

        Return:
            negative_balance_list (list[list]):  list with a list of all the information of the
            clients.
        """
        negative_balance_list = []
        for i in range(len(self.clients)):
            if self.clients[i][6] < 0:
                negative_balance_list.append(Bank.clients[i])
        return negative_balance_list

    def list_all(self) -> list[list]:
        """
        This function returns the list of the information of all clients.

        Return:
            list_clients (list[list]):  list with a list of all the information of the clients.
        """
        list_clients = []
        for i in range(len(self.clients)):
            list_clients.append(self.clients[i])
        return list_clients

    def delete_client(self, client) -> None:
        """
        This function removes the client from the list of clients.

        Attributes:
            client (object): The client.
        """
        client_in_list = False
        for i in range(len(self.clients)):
            for j in range(8):
                if self.clients[i][j] == client.client[j]:
                    client_in_list = True
            if client_in_list:
                del self.clients[i]
                break

    def object_to_file(self, file: str, option: str) -> None:
        """
        This function takes the clients and appends it into client.csv
        """
        with open(file, option, newline='') as file:
            writer = csv.writer(file)
            for i in range(len(self.clients)):
                writer.writerow(self.clients[i])
