#
# Python: 3.10.1
#
# Author: Serena Seyler
#
# Purpose: The Tech Academy, Class Inheritance demo

"""
    This is a basic class attribute setup for a bank account, every account has a user, so this is the parent.
    There are two types of users: Personal and Business
    The parent class is a generic 'User' class that includes basic contact information and account number
    common to any child classes created from the parent class. There are two child classes that inherit
    attributes from 'User', the 'Personal' class includes additional information such as social security number,
    date of birth, and opting in to paperless satements. The 'Business' user includes attributes for a tax Id number
    and a fax #
"""

# parent class, 'User' 
class User:
    name = ' ' # name
    email = ' ' #email
    street = ' ' # street address
    city = ' ' # city
    state = ' ' # state
    zipCode = 0 # zip code
    phone = ' ' # phone number
    acct = 0 # account number
    


# child class 'Personal', inherits from 'User'
class Personal(User):
    ssn = ' ' # social security number
    dob = ' ' # date of birth
    optInPaperless = False # opt in for paperless statements, false by default


# child class 'Business', inherits from 'User'
class Business(User):
    taxId = ' ' # tax id number
    fax = ' ' # fax number
