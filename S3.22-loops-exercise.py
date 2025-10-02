import random

print ("Exercise 1: get a list of names from the user and print a random one")

names = []

while len(names) < 8:
    new_name = input ("Please enter a name: ")
    names.append(new_name)

name_index = random.randint(0, len(names)-1)

print ("The name at index", name_index, "is", names[name_index])


print ("-------------------------------------------------")

print ("Exercise 2: guess a colour game")

colours=("blue", "green", "yellow", "red", "orange", "purple", "indigo", "violet", "grey", "white", "black", "pink")
playing=True

while playing:
    curr_colour_index = random.randint(0, len(colours)-1)
    print ("New Game! What colour am I thinking of?")
    print (colours)
    user_colour = ""

    while (user_colour != colours[curr_colour_index]):
        user_colour = input ("Guess a colour: ")
        user_colour = user_colour.lower()

        if (user_colour != colours[curr_colour_index]):
            print ("Sorry,", user_colour, "is not correct. Try again.")
        else:
            print ("You guessed it! My colour was", colours[curr_colour_index])

    replay = input ("Would you like to play again? (yes/no) ")
    replay = replay.lower()

    playing = replay != 'no'
    print ("---------------- End game ---------------------")
    
