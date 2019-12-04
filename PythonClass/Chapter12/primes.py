#primes.py

#by William Fuentes 12/3/19

def main():
    print("This program will list all primes leading up to to the limit.")
    n = int(input("What is the limit? "))

    #Initialize the main list and an empty prime list
    list = [i for i in range(2,n+1)]
    primeList = []
    

    #This loop whill check if there is anything left in the main list
    # if so, it will add the first number to the prime list, then
    # for a number in list, if the number mod the first number is 0,
    # it will remove the number, thus removing all multiples of the
    # first position in the list, and so on.
    while(True):
        if(len(list) == 0):
           break
        else:
            num = list[0]
            primeList.append(num)

            for i in list:
                if i % num == 0:
                    list.remove(i)

    #Finally, the prime list is printed.
    print(primeList)
    wait = input("Press Enter to exit.")

main()
