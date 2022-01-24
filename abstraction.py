#
# Python: 3.10.1
#
# Author: Serena Seyler
#
# Purpose: The Tech Academy, Abstraction demo


from abc import ABC, abstractmethod


# parent class
class Character(ABC):
    @abstractmethod
    def catchphrase(self, name):
        pass

    def typeOfCharacter(self, charType):
        print("I'm a {} character.".format(charType))

# child class
class Bart(Character):
    # override and define abstract method
    def catchphrase(self, name):
        print("I'm {}, Don't have a cow, man!".format(name))


# instantiate object
simpson = Bart()
simpson.catchphrase("Bart Simpson") # using child method
simpson.typeOfCharacter("main") # using parent method


