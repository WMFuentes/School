#lists.py
#by William Fuentes

#This program will generate a list of 50 numbers, random 1-100.
#It will then remove duplicates from the list.
#Then it will print the original and condensed lists.

#After discovering sets, I have simplified my code to be more efficient.
#I have commented out my old code to show the progress.
#The new version generates a list of 50 digits, then converts it to a set.

import random
import time

def main():
    print("The following lists are randomly generated. The first list ",
          "contains duplicates, while the second had duplicates removed.")
    print()

    #**Version 1** - Intitialize 2 lists, add 50 random digits to 1, check if
    #digit from list 1 is in list 2, if not, add to list 2. Print both lists.
    
    #original = []
    #condensed = []

    #for x in range(50):
        #x = random.randrange(1,101)
        #original.append(x)

    #for x in original:
        #if x not in condensed:
            #condensed.append(x)

    #**Version 2** - Initialize and populate 1 list, convert it to a set, then print
    #both list/set.

    start = int(time.time()*1000.0)
    original = []
    for x in range(5000000):
        x = random.randrange(1,10000000)
        original.append(x)

    condensed = set(original)
    end = int(time.time()*1000.00)
    timeToComplete = end - start
    #print("The original list of 50 items is:")
    #print(original)
    print()
    print("The condensed list containing {} items is :".format(len(condensed)))
    print("Time to complete: ", timeToComplete)
    #print(condensed)

    wait = input("Press Enter to exit.")

main()
