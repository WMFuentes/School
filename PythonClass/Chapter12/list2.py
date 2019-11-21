import random
import time

def main():
    print("The following lists are randomly generated. The first list ",
          "contains duplicates, while the second had duplicates removed.")
    print()
    original = []
    condensed = []
    start = int(time.time()*1000.0)
    for x in range(5000000):
        x = random.randrange(1,10000000)
        original.append(x)

    for x in original:
        if x not in condensed:
            condensed.append(x)

    end = int(time.time()*1000.00)
    timeToComplete = end - start
    #print("The original list of 50 items is:")
    #print(original)
    print()
    print("The condensed list containing {} items is :".format(len(condensed)))
    print("Time to complete: ", timeToComplete)
    #print(condensed)
main()
