#
# Python: 3.10.1
#
# Author: Serena Seyler
#
# Purpose: The Tech Academy, Nice or Mean text-based game where user must choose between being
#          nice or mean to a stranger and then face the consequences at the end



def start(nice = 0, mean = 0, name = ""):
    #get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)



# get name and display game rules
def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this uer's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if (name == ""):
                name = input("\nWhat is your name?\n>>> ").capitalize()
                if (name != ""):
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print(" but at the end of the game your fate \will be sealed by your actions.")
                    stop = False
    return name



# the main game function
def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M)\n>>>: ").lower()
        if (pick == "n"):
            print("\The stranger walkes away smiling...")
            nice = (nice + 1)
            stop = False
        if(pick == "m"):
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) # pass the 3 variables to score()



# function to output score to screen with passed in variables
def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


# depending on nice or mean score, the function will pass the variables to either win(),
#       lose(), lastChance(), or call nice_mean() again
def score(nice, mean, name):
    # score function is being passed the values stores within the 3 variables
    if(nice > 2): # call win function passing in the variables so it can use them
        win(nice, mean, name)
    if(mean > 2 and mean < 4): # call lose function passing in the variables so it can use them
        lastChance(nice, mean, name)
    if(mean > 4):
        lose(nice, mean, name)
    else:   # else, call nice_mean function passing in the variable so it can use them
        nice_mean(nice, mean, name)


# if user is nice, they win the game
def win(nice, mean, name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nYou've made lots of people smile today \nand you even found $20 on the ground, kindness pays off!".format(name))
    # call again function and pass in our variables
    again(nice, mean, name)



# if user is too mean, they lose the game
def lose(nice, mean, name):
    # Substitute the {} wildcards with our variable values
    print("\nYou were warned, {}, game over! \nBe kinder next time, \nyou made a baby cry, you overdrew your bank account \nand your cat threw up on your shoe!".format(name))
    print("\nIt doesn't pay to be mean!")
    # call again function and pass in our variables
    again(nice, mean, name)



# if user is about to lose, they are given one last chance to make it right
def lastChance(nice, mean, name):
    print("\nIt's not looking good for you, Ebineezer. \nIf you don't want a visit from three ghosts \ntonight, I suggest you try again, {}!\n".format(name))
    nice_mean(nice, mean, name)



# once the game is won or lost the user is given the option to play again or quit
def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if(choice == "y"):
            stop = False
            reset(nice, mean, name)
        if(choice == "n"):
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', ( N ) for 'No':\n>>> ")



# if user chooses to play again, reset the score but keep the name
def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)

    

if __name__ == "__main__":
    start()
