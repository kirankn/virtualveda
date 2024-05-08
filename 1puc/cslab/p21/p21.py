#function to remove the duplicate elements
def removeDup(list1):
#Checking the length of list for 'for' loop
    length = len(list1)
    #Defining a new list for adding unique elements
    newList = []
    for a in range(length):
    #Checking if an element is not in the new List
    #This will reject duplicate values
        if list1[a] not in newList:
            newList.append(list1[a])
    return newList

#Defining empty list
list1 = []
#Asking for number of elements to be added in the list
inp = int(input("How many elements do you want to add in the list? "))
print("Enter the elements: ")
#Taking the input from user
for i in range(inp):
    k=str(i+1)
    a = int(input(k+"> "))
    list1.append(a)

#Printing the list
print("The list entered is:",list1)
#Printing the list without any duplicate elements
print("The list without any duplicate element is:",removeDup(list1))
