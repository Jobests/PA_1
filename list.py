#getting the input of the user
n = input("Enter your  inputs seperated by spaces: ")

#coverting the numbers to list
writeyourcodehere = n.split()

#assign the first, the middle,the last integers
first, *middle, last = writeyourcodehere 

#print output
print("first: " + str(first))
print("middle: " + str(middle))
print("last: " + str(last))
