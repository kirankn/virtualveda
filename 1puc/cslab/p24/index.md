## 24. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string. Sample string : ‘2nd pu course’
Expected output : {‘ ‘:2, ‘2’:1, ‘n’:1, ‘d’:1, ‘o’:1, ‘p’:1, ‘u’:2, ’c’:1, ‘s’:1, ‘r’:1, ‘e’:1}

<!-- ### Flowchart
![Image](./p24.png) -->

### Program
[Download Source Code](./p24.py ':ignore')
```python
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
```

### Output

```bash
Enter a string: acceleration
{'a': 2, 'c': 2, 'e': 2, 'l': 1, 'r': 1, 't': 1, 'i': 1, 'o': 1, 'n': 1}
```

```bash
Enter a string: Mississippi
{'M': 1, 'i': 4, 's': 4, 'p': 2}
```