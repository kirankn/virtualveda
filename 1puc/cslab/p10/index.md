## 10. Write a program to find the sum of digits of an integer number, input by the user.

<!-- ### Flowchart
![Image](./p10.png) -->

### Program
```python
#Initializing the sum to zero
sum = 0
# Asking the user for input and storing it as a string
n = input("Enter the number: ")
# Looping through each digit of the string
# Converting it to int and then adding it to sum
for i in n:
    sum = sum + int(i)
# Printing the sum
print("The sum of digits of the number is",sum)
```

### Output

```bash
Enter the number: 12345
The sum of digits of the number is 15
```
### Source Code
[Download Source Code](./p10.py ':ignore')
