userInput = input("Write a sentence: ")
#Count the total number of characters in the text (including white spaces) which is the length of string
totalChar = len(userInput)
print("Total Characters: ",totalChar)
#Count the total number of alphabets,digit and special characters by looping through each character and incrementing the respective variable value
totalAlpha = totalDigit = totalSpecial = 0
for a in userInput:
    if a.isalpha():
        totalAlpha += 1
    elif a.isdigit():
        totalDigit += 1
    else:
        totalSpecial += 1
print("Total Alphabets: ",totalAlpha)
print("Total Digits: ",totalDigit)
print("Total Special Characters: ",totalSpecial)

#Count number of words (Assume that each word is separated by one space)
#Therefore, 1 space:2 words, 2 space:3 words and so on
totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1

print("Total Words in the Input :",(totalSpace + 1))
