## 21. Write a program to read a list of elements. Modify this list so that it does not contain any duplicate elements, i.e., all elements occurring multiple times in the list should appear only once.

<!-- ### Flowchart
![Image](./p21.png) -->

### Program
```python
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
```

### Output

```bash
How many elements do you want to add in the list? 5
Enter the elements: 
1> 10
2> 10
3> 15
4> 26
5> 15
The list entered is: [10, 10, 15, 26, 15]
The list without any duplicate element is: [10, 15, 26]
```
### Source Code
[Download Source Code](./p21.py ':ignore')
