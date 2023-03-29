# do a fibonacci sequence 

# do a loop to add x+y, shift number to right and redo


# expect 0, 1, 1, 2, 3, 5, 8, 13, 21, .... think shifting memory cells
#           x  y  z ----> going this way
x = 1 
y = 1 
z = 0
i = 0
while i < 9:
 if i == 0:
    print(i) # we have i at zero so use it
 if i == 1:
   print(x)
 if i == 2: # at 3 point in sequence
   print(x)
 if i > 2: # and now we get to add numbers together
   z = x + y
   print(z)
   x = y # shift values to right on seq this 1st or we overwright wrong cell
   y = z # and 2nd part of shift values 
 i += 1
