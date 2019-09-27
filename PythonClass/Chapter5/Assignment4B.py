# This program will add up the number value of each letter in a given
# name, provided by the user. Each letter corresponds to a number and
# is added to reach a total.

#by William Fuentes 9/26/2019

def main():
    # Gather the input of the name.
    name = input("Please provide your name:")

    # Initialize values for a list of the alphabet, change the name to a list
    # then start the accumulator at 0. I found the list() method by Googling
    # for a simple way to turn a string into a list of characters.
    # I put "space" at the beginning so its position = 0 when adding.
    alpha = [" ", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
             "p","q","r","s","t","u","v","w","x","y","z"]
    name = list(name)
    num = 0

    # This loop runs through each character of the name list, matches the
    # character with the position in alpha, using the index() method (a method
    # I found on Google to return the position a given character), then adds
    # that position to an accumulator.
    for i in name:
        num = num + alpha.index(i)

    print("The number of your name is: ", num)
    input("Press Enter to exit")

main()

# Part A and B do very similar things. They break a large string down into
# smaller elements and then adds those elementes up in a loop and accumulator.
# Part A is a bit easier because we do not have to assign a value to each
# item of a list.
# Part B required a bit of elbow grease and Googling to find a good method to
# complete this task the best way. It reminded me of a broken down HashMap
# from Java, where 1 key is mapped to a value. In this case, a letter is mapped
# to an integer value.
