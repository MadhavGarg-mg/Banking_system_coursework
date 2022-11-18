# CSC1034: Project 2

This package is built as a part of CSC1034: Project 2.

This is a simple banking application that can handle the need of more than 100 clients. The application can add, 
edit, and delete clients. It can also help clients withdraw and deposit their money. We can also
get a list of all the clients in the bank and also sort them according to their first name, last name,
date of birth, and if they have negative balances. We can also put all the clients in a csv file and retrieve them
directly from the csv when we have to.

---


## Creating a client
We can create a client by putting the objects such as title, first name, last name, pronouns, date of birth,
occupation, account balance, and overdraft limit in Client.

john_king = Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100) adds a client to 
the list of clients automatically.

We have to make sure all the objects are the correct types otherwise the code will give a type error.

---

## Representing a client
We can represent the client in 2 ways:
*     __str__() 
*     __repr__() 

---
## Getting client information
We can get all the information for a client using the getter functions.


Example for the getter functions:
*     get_title(): Gives the title of the client.
*     get_first_name(): Gives the first name of the client.
*     get_last_name(): Gives the last name of the client.
*     get_pronouns(): Gives the pronouns of the client.
*     get_date_of_birth(): Gives the date of birth of the client.
*     get_occupation(): Gives the occupation of the client.
*     get_account_balance(): Gives the account balance of the client.
*     get_overdraft_limit(): Gives the overdraft limit of the client.

I have also made the date of birth, account balance, and the overdraft limit of a client as a private 
attributes to add privacy for the user's sensitive information.

---

## Deposit money
The client can deposit money into the client's bank account. They need to put an amount to deposit, and 
it will be reflected accordingly in the client's account balance.

I am raising a typeError for a negative amount as putting a negative value accidentally would 
decrease the amount from the account balance.

*     deposit(arg): This function can deposit money to the client's account.

---

## Withdraw money
The client can withdraw money from the client's bank account. They need to put an amount to withdraw,
and it will be reflected accordingly in the client's account balance. If the client withdraws 
enough money to go beyond their overdraft limit, then any withdraws made while the client is below their 
overdraft limit will add an extra fee of 5.

I am raising a typeError for a negative amount as putting a negative value accidentally would
increase the amount to the account balance.

*     withdraw(arg): This function can withdraw money from the client's account.

---

## Setting client information
We can use the setter function to edit the client details such as name, first name, last name, 
pronouns, date of birth, occupation, and overdraft limit. We are not allowed to edit the client 
account balance using the setter, we can edit the account balance only using deposit and withdraw.
Putting an argument that is not of the allowed type will raise a typeError.

We have the following setter functions:
*     set_title(arg): Sets the new title for a client.
*     set_first_name(arg): Sets the new first name for a client.
*     set_last_name(arg): Sets the new last name for a client.
*     set_pronouns(arg): Sets the new pronouns for a client.
*     set_date_of_birth(arg): Sets the new date of birth for a client.
*     set_occupation(arg): Sets the new occupation for a client.
*     set_overdraft_limit(arg): Sets the new overdraft limit for a client.
---

## Sorting functions
We can sort the list of all clients by using the list_by functions. The assumption here is that
the arguments passed by the user will be case-sensitive.

We can sort the clients in 4 ways:
*     list_by_first_name(arg): Returns a list of all the clients that have the same first name as the argument. 
*     list_by_last_name(arg): Returns a list of all the clients that have the same last name as the argument.
*     list_by_birthday(arg): Returns a list of all the clients that have the same birthday as the argument.
*     list_by_negative_balance(): Returns a list of all the clients that have a negative account balance.
---

## list all
We can also get a list of all the clients in the bank using the list all function.

*     list_all()

---

## Delete client
We can also delete a client from the list of clients. 

*     delete_client(arg): Argument is the client.

---

## Client to file
We can also put all the clients into a file, we can write all the clients to the file, or can append 
new clients to a file.

*     object_to_file(arg1, arg2): Argument1 is the file we want to add clients into, and the argument2 is the mode(write or append) we
      want to choose.

---

## Data retrieval
We can also retrieve our clients from the file we create and use them to run functions.

*     file_to_list_object(arg): Argument is the file from which the data will be retrieved.

---
