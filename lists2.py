#Python program to calculate the average value of a list elements.

mylist = [20, 30, 25, 35, -16, 60, -100]

denominator = len(mylist)   # what to divide by 
listtotal = 0 # total to divide

for x in mylist:
    listtotal += x 

print ("The average of my list is %.2f" % (listtotal/denominator)) #one liner to do calc and format output
