# CSC1034: Project 2

This package is build as a part of the CSC1034: Project 2.

This is a simple banking application that can handle the need of more than 100 clients. The application can add, 
edit, and delete clients. It can also help the clients withdraw and deposit their money. We can also
get a list of all the clients in the bank and also sort them according to their first name, last name,
date of birth, and if they have negative balance. We can also put all the clients in a csv file and retrieve them
directly from the csv when we have to.

---

### Creating a client
We can create a client by putting the objects such as title, first name, last name, pronouns, date of birth,
occupation, account balance, and overdraft limit in Client.

Example to add a client:
```
john_king = Client('Mr', 'John', 'King', 'He/Him', date(2002, 12, 31), 'Student', 1000, 100)
```
We have to make sure all the objects are the correct types otherwise the code will give a type error.


---

### Representing a client
We can represent the client in 2 ways:
1. Using the __str__ representation. 
2. Using the __repr__ representation.

Example for the __str__ representation:

```
print(john_king.__str__())
```
Example for the __repr__ representation:

```
print(john_king.__repr__())
```
---
### Getting client information
We can get any information for a client using the getter functions.

Example for the getter functions:

```
print(john_king.get_title())
print(john_king.get_first_name())
print(john_king.get_last_name())
print(john_king.get_pronouns())
print(john_king.get_date_of_birth())
print(john_king.get_occupation())
print(john_king.get_account_balance())
print(john_king.get_overdraft_limit())
```

I have also made the date of birth, account balance ,and the overdraft limit of a client as private 
attributes to add privacy for the user's sensitive information.

---

### Deposit money
The client can deposit money into the client's bank account. They need to put an amount to deposit, and 
it will be reflected accordingly in the client's account balance.

I am raising a typeError for a negative amount as putting a negative value accidentally would 
decrease the amount from the account balance.

Example for depositing money in the client's account:
```
john_king.deposit(100)  # This code will increase the account balance by 100.
john_king.deposit(-100)  # This code will raise typeError
```

---

### Withdraw money
The client can withdraw money from the client's bank account. They need to put an amount to withdraw,
and it will be reflected accordingly in the client's account balance. If the client withdraws 
enough money to go beyond their overdraft limit, then any withdraws made while the client is below their 
overdraft limit will add an extra fee of 5.

I am raising a typeError for a negative amount as putting a negative value accidentally would
increase the amount to the account balance.

Example to withdraw money from the client's account.
```
john_king.withdraw(100)  # This code will decrease the account balance by 100.
john_king.withdraw(-100)  # This code will raise typeError
```
---

### Setting client information
We can use the setter function to edit the client details such as name, first name, last name, 
pronouns, date of birth, occupation, and overdraft limit. We are not allowed to edit the client 
account balance using the setter, we can edit the account balance only using deposit and withdraw.

Example for the setter functions:

```
print(john_king.set_title('Dr'))
print(john_king.set_first_name('Jon'))
print(john_king.get_last_name('Kingston'))
print(john_king.get_pronouns('They/Them'))
print(john_king.get_date_of_birth(date(2000, 1, 1)))
print(john_king.get_occupation('Lawyer'))
print(john_king.get_overdraft_limit(200))
```
---

