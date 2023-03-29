# get number inout and check if it is a prime number


# if it is not 2 but divisable by 2 it is not a prime number

# if it is negative 0 or 1 it is not a prime number

inputNumber = int(input("Enter a whole number to find if it is prime: "))


#if it is odd then do loop dividing by lower and lower numbers until it reaches 1

def checkForPrime(inputNumber):
    if inputNumber < 0:
        print("Cant have a negative number")

    i = inputNumber 
    dividebymultipletimes = 0 #counter for times it was successfully divided into a whole number lower than it
    while i > 1:
        if inputNumber % i == 0:
            dividebymultipletimes += 1 #increment successful division into whole number
        i -= 1
    if dividebymultipletimes == 1:
        print("is prime")
    else:
        print("is not prime")
    


checkForPrime(inputNumber)
