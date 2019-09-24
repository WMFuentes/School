# futval.py
#    A program to compute the value of an investment
#    carried however many years into the future, as you can choose.
#   by William Fuentes

# Gather inputs: principal, interest rate, and investment years
# Calculate the yield for a quarterly compounding period
# Loop through the calculation, 4 times per year (quarterly)
# Print the calculated results

def main():
    print("This program calculates the future value")
    print("of an investment, compunded quarterly.")

    # Here we will gather inputs: principal, interest rate, and years
    # to invest, keeping in mind this investment compunds quarterly.
    
    principal = eval(input("Enter the initial principal amount: "))
    rate = eval(input("Enter the annual interest rate as a decimal: "))
    years = eval(input("Enter the number of years (at least 10): "))
    
    # We could also accept inputs all at once with the following:
    #principal,rate,years = eval(input("Enter the principal, annual interest rate, and years separated by commas"))


    # This loop will process our equation 4 times a year (quarterly compounding)
    # The equation has been edit to divide the stated interest by 4 as well.
    
    for i in range(years*4):
        principal = principal * (1 + (rate/4))

    # To test our loop, I have the equation below. See comments at bottom.
    #principal = principal * ((1 + rate/4)**(years*4))

    print("The value in 10 years is:", principal)
    
    # The input line is entered so it won't close out of the cmd window.
    input("Press Enter to exit.")

main()

# I have a finance background and have done this equation countless times by hand.
# It made me curious as to why we would run this through a loop rather than the equation.
# in this program, we could replace the loop with the following:
# principal = principal * ((1 + rate/4)**(years*4)).
# I used this as a test to make sure it gave the same answers as our loop. It is added above,
# but commented out so it is easy to add # to the loop and delete the one by the equation.
