import random

# Declaring the list of values
randomList = []

# Generate random list of 5 values between 1 and 30
# example [1, 22, 5, 6, 10]
for i in range(0,5):
    n = random.randint(1,30)
    randomList.append(n)

# Print the list content
print(randomList)