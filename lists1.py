#Write a Python program to sum values of a list.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # numbers to add
listtotal = 0 # total for calc

for x in mylist:
    listtotal += x # add from list element to running total

print(listtotal) # once out loop print total
