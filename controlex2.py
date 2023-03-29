# Python Program - Get 2 Integers Input from User and check increasing or decreasing
num1 = int(input("Enter 1st Integer: ")) #1st entry
num2 = int(input("Enter 2nd Integer: "))
num3 = int(input("Enter 2nd Integer: "))


if num1 < num2 and num2 < num3: # cant compare 3 at once so use "and", check for increasing
    print("Increasing order") 
elif num1 > num2 and num2 > num3: # compare and check for decreasing
    print("Decreasing order")
else:                               #all other condistions
    print("Neither increasing or decreasing order")
