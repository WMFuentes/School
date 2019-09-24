# File: chaos.py
# A simple program illustrating chaotic behavior.
# by William Fuentes

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        # The multiplier has been changed to 2.0 from 3.9.
        x = 2.0 * x * (1 - x)
        print(x)
    wait = input("PRESS ENTER TO CONTINUE.")
    
main()

# Changing the equation to 2.0 from 3.9 reduced the chaotic nature of the output.
# I tested this out with several different multipliers, such as 3.0 and 2.9 and found 
# that the chaotic nature of the output is not as great as 3.9. I then experimented
# by extending the loop to 100 instances. Compared to 3.9, 2.0 ends its chaotic outputs
# after 4 loops, ending with 0.5.
