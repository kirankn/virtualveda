#Count the number of times a character appears in a given string
st = input("Enter a string: ")

dic = {}
#creates an empty dictionary

for ch in st:
    if ch in dic:
        #if next character is already in the dictionary
        dic[ch] += 1
    else:
        #if ch appears for the first time
        dic[ch] = 1

#Printing the count of characters in the string
print(dic)
