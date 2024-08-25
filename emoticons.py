#declare set of values
words = {"smile": ":)", "grin": ":D", "sad": ":(", "mad": ">:("}

#output options
print("These are the only words that can be turned into emoticons: " + str(words))

#get user input
n = input("Use any of these words in a sentence: ")

#function to replace keys with values
def emotify(n):
    for key, values in words.items():
        n = n.replace(key, values)
    print(n) #output the results

#calling the function
emotify(n)