# This program counts the number of words in a string.
# It assumes the string can span more than one line,
# the sentence will end in a period, and
# the words could be separated by a space, comma, or both.

# by William Fuentes 9/26/2019

def main():
    print("This program will count the number of words in a given sentence.")

    # Here we take the input of the sentence.
    string = input("Please type a sentence: ")

    # The following loop splits the sentence into a list, then adds 1 for each
    # element of the list.
    words = 0
    for i in string.split():
        words = words + 1

    # After the elements are counted, they are printed.
    print("Your orignal sentence is:", string)
    print("This sentence contains", words, "words.")
    
    input("Press Enter to exit.")

main()

# Part A and B do very similar things. They break a large string down into
# smaller elements and then adds those elementes up in a loop and accumulator.
# Part A is a bit easier because we do not have to assign a value to each
# item of a list.
# Part B required a bit of elbow grease and Googling to find a good method to
# complete this task the best way. It reminded me of a broken down HashMap
# from Java, where 1 key is mapped to a value. In this case, a letter is mapped
# to an integer value.
