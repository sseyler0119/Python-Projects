#
# Python: 3.10.1
#
# Author: Serena Seyler
#
# Purpose: The Tech Academy, Encapsulation demo


# demo class Account
class Account:
    # initializer
    def __init__(self):
        self.__accountNum = 0 # private variable, initialze to 0
        self._name = 'No name' # protected variable, initialize to 'No name' string

    # accessor function to output name and account number
    def getAccountNum(self): 
        print("{} \nAccount Number: {}".format(self._name,self.__accountNum))

    # mutator function to set private and protected variables
    def setAccountNum(self, name, accountNum):
        self.__accountNum = accountNum
        self._name = name


account = Account() # instantiate Account object
account.getAccountNum() # get current Account info
account.setAccountNum('Jasper Smith', 5469874) # set account number
account.getAccountNum() # output updated account info
