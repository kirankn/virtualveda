## 6. Write a program that takes name and age of the user as input and displays a message whether the user is eligible to apply for a driving license or not. The eligible age is 18.

<!-- ### Flowchart
![Image](./p6.png) -->

### Program
[Download Source Code](./p6.py ':ignore')
```python
#Program to check the eligibility for driving license
name = input("What is your name? ")
age = int(input("What is your age? "))

#Checking the age and displaying the message accordingly
if age >= 18:
    print("You are eligible to apply for the driving license.")
else:
    print("You are not eligible to apply for the driving license.")
```

### Output

```bash
What is your name? John
What is your age? 23
You are eligible to apply for the driving license.
```
```bash
What is your name? Jack
What is your age? 16
You are not eligible to apply for the driving license.
```
