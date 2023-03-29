multiplier = int(input("Which multiplication table do you want 1-10:")) #user entry cast to int

i = 1 # for 1x whatever
result = 0
while i <= 10: # up to x10
    result = i * multiplier # calculation
    print("%d x %d = %d" % (i, multiplier, result)) # format for int
    i += 1