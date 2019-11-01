#Chapter 8, exercise 9 and 10.
#This program calculates fule efficiency from either user input or file input.
#It requires the miles driven and gallons of gas used as inputs to calculate
#the MPG for the trip.
#Users have a choice to enter the information or provide a file with the inputs.
#by William Fuentes

def main():
    #Ask user to input manually or with a file.
    print("This program helps you calculate the fuel efficiency of your trip.")
    choice = input("Would you like to import trips from a file? (Y/N):")
    
    #Based on the input, call either the interactive or file input calculator.
    if choice[0] == "y" or choice[0] == "Y":
        fileMPG()
    else:
        manualMPG()

#manualMPG has the user input each leg of the trip and summarizes the trip with a blank line.
def manualMPG():
    startMiles = int(input("Enter the beginning odometer miles: "))

    totalMiles = 0
    totalFuel = 0

    entry = input("Enter the trip leg's odometer reading and gallons of fuel used, separated by a space:")

    #This loop will continue until the user enters a blank line.
    while entry != "":

        #The initial entry is split into 2 positions of a list, miles and gallons used.
        legList = entry.split()
        legMiles = int(legList[0])
        legFuel = int(legList[1])

        #MPG is calculated and then printed.
        efficiency = (legMiles - (startMiles + totalMiles)) / legFuel
        print("This leg's miles per gallon is ",efficiency,".")

        #Total miles and fuel are calculated for the final print.
        totalMiles = legMiles - startMiles
        totalFuel += legFuel

        #Request for a new leg of the trip.
        entry = input("Enter the trip leg's odometer reading and gallons of fuel used, separated by a space."
                      " Hit Enter to summarize the trip.")

    print("The total miles per gallon (MPG) is", totalMiles / totalFuel,".")
    
#This will allow the user to access a file with all of the data.
def fileMPG():

    #Reqest the file from the user. I have included triplog.txt to test.
    fileName = input("What file are the trips in? ")
    infile = open(fileName,'r')

    #The rest of this program mimics the manual process, but pulls the inputs from the file.
    startMiles = int(infile.readline())

    totalMiles = 0
    totalFuel = 0
    leg = 1

    entry = infile.readline()

    #This loop again will break at the end of the file, when there is an empty line.
    while entry != "":

        legList = entry.split()
        legMiles = int(legList[0])
        legFuel = int(legList[1])

        efficiency = (legMiles - (startMiles + totalMiles)) / legFuel

        print("Leg",leg,"miles per gallon is ",efficiency,".")

        totalMiles = legMiles - startMiles
        totalFuel += legFuel
        leg += 1

        entry = infile.readline()

    #Closing the file.
    infile.close()

    print("The total miles per gallon (MPG) is", totalMiles / totalFuel,".")

#Per chapter 7, this guarantees that main will automatically run.
if __name__ == '__main__':
    main()
