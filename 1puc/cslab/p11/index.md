## 11. Write a program to check whether an input number is palindrome or not.

Note: A number or a string is called palindrome if it appears same when written in reverse order also. For example, 12321 is a palindrome while 123421 is not a palindrome

<!-- ### Flowchart
![Image](./p11.png) -->

### Program
```python
#program to find if the number is a palindrome
rev = 0
n = int(input("Enter the number: "))
#Storing the number input by user in a temp variable to run the loop
temp = n
#Using while function to reverse the number
while temp > 0:
    digit = (temp % 10)
    rev = (rev * 10) + digit
    temp = temp // 10
#Checking if original number and reversed number are equal
if(n == rev):
    print("The entered number is a palindrome.")
else:
    print("The entered number is not a palindrome.")
```

### Output

```bash
Enter the number: 12321
The entered number is a palindrome.
```

```bash
Enter the number: 1234
The entered number is not a palindrome.
```

### Source Code
[Download Source Code](./p11.py ':ignore')
