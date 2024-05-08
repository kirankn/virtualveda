## 16. Write a program to input line(s) of text from the user until enter is pressed. Count the total number of characters in the text (including white spaces), total number of alphabets, total number of digits, total number of special symbols and total number of words in the given text. (Assume that each word is separated by one space.)

<!-- ### Flowchart
![Image](./p16.png) -->

### Program
```python
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
```

### Output

```bash
Write a sentence: the quick brown fox jumps over the lazy dog
Total Characters:  43
Total Alphabets:  35
Total Digits:  0
Total Special Characters:  8
Total Words in the Input : 9
```

```bash
Write a sentence: Hi, I'm selling delicious burgers today for $3 each!
Total Characters:  52
Total Alphabets:  39
Total Digits:  1
Total Special Characters:  12
Total Words in the Input : 9
```

### Source Code
[Download Source Code](./p16.py ':ignore')
