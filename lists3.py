# find high and low from list

highValue = 0
lowValue = 0

myList = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
print("Original list: %s"%(myList)) #print list before sorting it
# myListLen = len(myList)

myList.sort() #sort list ascending

lowValue = myList[0] #find 1st element
highValue = myList[len(myList)-1] # find last element
print("Low value : %d" %(lowValue)) #print values
print("High value: %d" %(highValue))
