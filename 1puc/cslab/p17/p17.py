#Changing a string to title case using title() function
def convertToTitle(string):
    titleString = string.title();
    print("The input string in title case is:", titleString)
userInput = input("Write a sentence: ")
#Counting the number of space to get the number of words
totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1
if(totalSpace == 0):
    #If the string is of one word only
    print("The input string is of one word only") 
elif(userInput.istitle()):
    #If the string is already in title case
    print("The input string is already in title case")
else:
    #If the string is not in title case and consists of more than one word
    convertToTitle(userInput)
