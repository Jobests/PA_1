#use function to sort out the words into alphatbetical order 
def alphabet_soup(a):
    b = ''.join(sorted(a))
    return b

#get user input
a = input("Enter word: ")

#call the function
b = alphabet_soup(a)

#output the result
print(b)