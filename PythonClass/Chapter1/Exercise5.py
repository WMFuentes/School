# File: chaos.py
# A simple program illustrating chaotic behavior.
# by William Fuentes

def main():
    print("This program illustrates a chaotic function")
    # Below has the new line to ask how many lines are to be printed.
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        # the range has been changed to n so it takes the input from 3 lines above.
        x = 3.9 * x * (1 - x)
        print(x)
    wait = input("PRESS ENTER TO CONTINUE.")
    input("Press enter to exit :)")

main()
