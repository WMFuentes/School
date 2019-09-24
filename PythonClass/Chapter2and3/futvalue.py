#Better_FV
# This program calculates the future value of money two different ways.
# by William Fuentes



def equationfv():
    print("This program will calculate the future value of money.")
    
    principal, apr, year = eval(input("Enter the principal, rate in decimal, and years to compound, separated by commas: "))
    #apr = eval(input("Enter the rate in decimal: "))
    #year = eval(input("Enter the number of years to compound interest: "))

    fv = principal * ((1 + apr)**year)

    print("After ",year," year(s), your money is worth ",fv)
    input("Press Enter to exit.")

#equationfv()

def loopfv():
    print("This progam calculates the future value of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter tha annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is: ",principal)
    input("Press Enter to exit.")

#loopfv()
