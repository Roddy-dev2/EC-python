# Python Program - Get 3 Integers Input from User and check matching
num1 = int(input("Enter 1st Integer: ")) #1st entry
num2 = int(input("Enter 2nd Integer: "))
num3 = int(input("Enter 2nd Integer: "))


if num1 == num2 and num2 == num3: # cant compare 3 at once so use and
    print("all the number are the same") 
elif num1 != num2 and num2 !=num3: # compare not equal
    print("all the numbers are diffrent")
else:                               #all other condistions
    print("Neither all are equal or different")
