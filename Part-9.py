# Object Oriented Programming( OOP's)
# Classes and Objects


# class Student:
#
#     counter = 1                     # class variable
#
#     def __init__(self, name):
#         # instance variable                             # __init__ : underscores are known as Dunders.
#         print("constructing")                           # init is basically initializer, default constructor in C++
#         self.n = name                                  # self is same as this in C++...and it automatically identifies
#         self.roll = Student.counter                     # which object is called...
#         Student.counter+=1


# s1 = Student('Bhumika')
# print(s1)
# s1.name = 'Bhumika'
# print(s1.name)
# s1.roll = 1
# print(s1.n, s1.roll)

# s2 = Student("Neha")
# print(s2.n, s2.roll)

# s1.counter = 300                                            # new counter attribute is made in object s1
# print(Student.counter)
# print(s1.counter)
# print(s2.counter)


# class Student:
#
#     counter = 0
#
#     def __init__(self, name):               # self is a pointer pointing to any instance..It can be s1,s2,....
#         print("creating object")              # name and roll no. are properties of student
#         self.name = name
#         self.roll_no = Student.counter
#         Student.counter += 1
#
#     def __str__(self):
#         return f"{self.roll_no}. {self.name}"
#
#
# s1 = Student('Anne')
# print(s1.name, s1.roll_no)
# print(str(s1))
# s2 = Student("billi")
# print(s2.name, s2.roll_no)
# print(s2)                            # print() automatically converts the output into string and then displays it....


# Multi line strings
# s='''
# this method is used to create a multi line string, also known as template string
# <html>
#     <body>
#         hello
#     </body>
# </html>
#
# '''
# print(s)


# Creating Bank Account class

'''
class Account
-- id( auto increment)
-- bal( mandatory)
a1,a2
Acc 1(acc. no.) has 100(balance)
'''


# class Account:
#     accountno = 1001
#
#     def __init__(self, bal=0):               # default argument
#         self.__balance = bal if bal>=0 else 0    # _ shows that you should not change the variable...and __ shows that
#         self.account_no = Account.accountno         # now nobody can update or change the value except the developer
#         Account.accountno += 1
#
#     def __str__(self):
#         return f"Account {self.account_no} has {self.__balance}"
#
#     def deposit(self, val):                        # custom methods...methods are functions inside class
#         if val > 0:
#             self.__balance += val
#
#     def withdraw(self, val):
#         if self.__balance >= val > 0:
#             self.__balance -= val
#
#
# a1 = Account(100)
# a2 = Account()
# a1.__bal = 99999                              # name mangling
# print(a1)
# print(a2)
# a2.deposit(100)
# a1.deposit(-1000)
# a2.withdraw(-1)
# a2.deposit(10)
# a2.withdraw(1000)
# Account.deposit(a1, 50)
# print(a2)
# a1.withdraw(100)
# print(a1)


# class Account:
#     accountno = 1001
#
#     def __init__(self, bal=0):               # default argument
#         self.__balance = bal if bal >= 0 else 0    # _ shows that you should not change the variable...and __ shows that
#         self.account_no = Account.accountno         # now nobody can update or change the value except the developer
#         Account.accountno += 1
#         self.trans = 0
#         self.maxTrans = 3
#
#     def __str__(self):
#         return f"Account {self.account_no} has {self.__balance}"
#
#     def deposit(self, val):                        # custom methods...methods are functions inside class
#         if val > 0 and self.trans < self.maxTrans:
#             self.__balance += val
#             self.trans += 1
#
#     def withdraw(self, val):
#         if self.__balance >= val > 0 and self.trans < self.maxTrans:
#             self.__balance -= val
#             self.trans += 1
#
#     def getBalance(self):
#         return self.__balance
#
#     def addInterest(self, amount):
#         self.__balance += amount
#
#
# class SavingsAccount(Account):
#     def getInterest(self):
#         return self.getBalance()*0.06
#
#     def addInterest(self):
#         interestAmount = self.getInterest()
#         super().addInterest(interestAmount)
#
#
# class CurrentAccount(Account):
#     def __init__(self, opening_bal=0):
#
#         super().__init__(opening_bal)                  # we get reference/ access to init() of base class
#         self.maxTrans = 4
#
#     def addInterest(self, amount):
#         pass

# ca1 = CurrentAccount()
# ca1.deposit(100)
# ca1.deposit(10)
# ca1.withdraw(10)
# ca1.withdraw(10)
# ca1.withdraw(10)
# print(ca1)

# ca2 = CurrentAccount(100)
# print(ca2)


# sa1 = SavingsAccount()
# sa1.deposit(100)
# sa1.deposit(10)
# sa1.withdraw(10)
# sa1.withdraw(10)
# print(sa1)
# print(sa1.addInterest())
# print(sa1)

# ca1 = CurrentAccount()
# ca1.deposit(100)
# ca1.addInterest(100)
# print(ca1)

# sa2 = SavingsAccount()
# sa2.deposit(100)
# sa2.deposit(10)
# sa2.withdraw(10)
# sa2.withdraw(10)
# print(sa2)
# print(sa2.addInterest())
# print(sa2)







