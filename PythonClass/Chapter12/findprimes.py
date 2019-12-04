#findprime.py
#by William Fuentes

#This program will find all primes between 1 and the number given by the user.

def main():
    print("This program will list all primes leading up to a given limit.")
    n = int(input("What is the limit? "))

    #Initialize the list
    primes = []

    #These nested for loops will count from 1 to the limit, divide a number
    # p by a number i in range 
    for p in range(1, n+1):
        for i in range(2,p):
            if p % i == 0:
                break
        else:
            primes.append(p)


    print("The prime numbers up to the limit are:")
    print(primes)
    wait = input("Press Enter to exit.")

main()
