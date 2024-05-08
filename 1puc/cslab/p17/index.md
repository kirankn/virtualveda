## 17. Write a user defined function to convert a string with more than one word into a title case string where string is passed as parameter. (Title case means that the first letter of each word is capitalized.)

<!-- ### Flowchart
![Image](./p17.png) -->

### Program
```python
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
```

### Output

```bash
Write a sentence: the quick brown fox jumps over the lazy dog
The input string in title case is: The Quick Brown Fox Jumps Over The Lazy Dog
```

```bash
Write a sentence: Makes Sense
The input string is already in title case
```

```bash
Write a sentence: Superb
The input string is of one word only
```

### Source Code
[Download Source Code](./p17.py ':ignore')
