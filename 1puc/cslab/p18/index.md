## 18. Write a function that takes a sentence as an input parameter where each word in the sentence is separated by a space. The function should replace each blank with a hyphen and the return the modified sentence.

<!-- ### Flowchart
![Image](./p18.png) -->

### Program
[Download Source Code](./p18.py ':ignore')
```python
# replaceChar function to replace space with hyphen
def replaceChar(string):
    return string.replace(' ','-')

userInput = input("Enter a sentence: ")

# Calling the replaceChar function to replace space with hyphen
result = replaceChar(userInput)

# Printing the modified sentence
print("The new sentence is:",result)
```

### Output

```bash
Enter a sentence: The quick brown fox jumps over the lazy dog
The new sentence is: The-quick-brown-fox-jumps-over-the-lazy-dog
```
