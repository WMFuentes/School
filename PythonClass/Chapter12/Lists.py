#lists.py
#by William Fuentes

#This program will generate a list of 50 numbers, random 1-100.
#It will then remove duplicates from the list.
#Then it will print the original and condensed lists.

import random

def main():
    #The greeting is printed.
    print("The following lists are randomly generated. The first list ",
          "contains duplicates, while the second had duplicates removed.")
    print()

    #Intitialize 2 lists, the orignial and condensed list.
    original = []
    condensed = []

    #The first loop generates a random number between 1 and 100, then adds
    #that number to the list titled original.
    for x in range(50):
        x = random.randrange(1,101)
        original.append(x)

    #The second loop iterates through the original list. If the element is not
    #in the new condensed list, the loop will add it. This way it only adds
    #one instance of each element.
    for x in original:
        if x not in condensed:
            condensed.append(x)

    #Now the results are printed.
    print("The original list of 50 items is:")
    print(original)
    print()
    print("The condensed list containing {} items is :".format(len(condensed)))
    print(condensed)

main()
