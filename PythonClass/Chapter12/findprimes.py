#findprime.py
#by William Fuentes

#This program will find all primes between 1 and the number given by the user.

def main():
    print("This program will list all primes leading up to 100.")

    primes = []

    for p in range(2, 101):
        for i in range(2,p):
            if p % i == 0:
                break
        else:
            primes.append(p)

    print(primes)

main()
