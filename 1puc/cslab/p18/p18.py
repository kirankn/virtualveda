# replaceChar function to replace space with hyphen
def replaceChar(string):
    return string.replace(' ','-')

userInput = input("Enter a sentence: ")

# Calling the replaceChar function to replace space with hyphen
result = replaceChar(userInput)

# Printing the modified sentence
print("The new sentence is:",result)
