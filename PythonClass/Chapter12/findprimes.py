#findprime.py
#by William Fuentes

#This program will find all primes between 1 and the number given by the user.

def main():
    print("This program will list all primes leading up to the provided number.")
    x = int(input("Please enter a number > "))

    primes = []
    y = 2

    for i in range(x):
        primes.append(i)

    for i in primes:
        if (i % y) == 0:
            primes.remove(i)
            y = y+ 1

    print(primes)

main()
