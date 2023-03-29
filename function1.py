# write 2 functions, show list content and find highest valve

myList = [10, 2, 3, 4 ,7]

def show_list(printedList):# list as value
    print("The content of the list is: %s" % (printedList))#print list

def find_print_max(evalList): #take list as value
    maxValue = max(evalList) #not sorting so functiosns can be run repeatedly
    print("The maximum of the list is: %s" % (maxValue))# print local value


show_list(myList) #run both functions, works in either order
find_print_max(myList)