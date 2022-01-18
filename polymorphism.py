#
# Python: 3.10.1
#
# Author: Serena Seyler
#
# Purpose: The Tech Academy, Class Inheritance and Polymorphism demo

#parent class
class Simpsons:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # print out character stats
    def catchphrase(self):
        msg = "\nHi, I'm {}, {}, \nWelcome to Springfield!".format(self.name, self.job)
        return msg

# child class
class Bart(Simpsons):
    #initializer
    def __init__(self, name, job, hobby, bully):
        super().__init__(name, job) # parent class initializer
        self.hobby = hobby # hobby belongs to Bart class
        self.bully = bully # bully belongs to Bart class
        
    # print out character stats
    def catchphrase(self):
        msg = "\nHi, I'm {}, {}, 'Don't have a cow, man!\nMy hobby is {}\n{} is my bully.".format(self.name, self.job, self.hobby, self.bully)
        return msg

# child class
class SideCharacter(Simpsons):
    #initializer
    def __init__(self, name, job, phrase, shirtColor):
        super().__init__(name, job) # parent class initializer
        self.phrase = phrase # phrase belongs to SideCharacter class
        self.shirtColor = shirtColor  # shirt belongs to SideCharacter class
        
        
    # print out character stats
    def catchphrase(self):
        msg = "\nI'm {}, {}\n{}\nI always wear a {}.".format(self.name, self.job, self.phrase, self.shirtColor)
        return msg


if __name__ == "__main__":

    mayor = Simpsons('Mayor Quimby', 'town mayor')
    print(mayor.catchphrase())
    boy = Bart('Bart Simpson','4th Grader', 'harrasing Principal Skinner', 'Nelson Muntz')
    print(boy.catchphrase())
    ned = SideCharacter('Ned Flanders','owner of the Leftorium', 'Hi-diddly-ho, neighborino!', 'green sweater with a pink button up underneath')
    print(ned.catchphrase())
