# get a factoral of a number
# ask user for number
userNum = int(input("Enter a whole number to get a factoral: "))


# use number in function to get factoral and print 

def find_factoral_from(inputNumber):
    if inputNumber < 0:
        print("Sorry negative numbers can't have a factoral") # minor validation
    factoralResult = 1
    i = 1  #setup vars for loop
    while i <= inputNumber: 
        factoralResult = factoralResult * i #calculate
        i += 1 # itterate loop var  
    print("The factoral of your number is: %d" % (factoralResult)) #finally print result


find_factoral_from(userNum) # call function
