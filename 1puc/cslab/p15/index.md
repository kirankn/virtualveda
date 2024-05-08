## 15. Write a program that has a user defined function to accept 2 numbers as parameters, if number 1 is less than 2 then numbers are swapped and returned , i.e., number 2 in place of number 1 is reformed in place of number 2, otherwise the same order is returned.

<!-- ### Flowchart
![Image](./p15.png) -->

### Program
```python
#defining a function to swap the numbers
def swapN(a, b):
    if(a < b):
        return b,a
    else:
        return a,b

#asking the user to provide two numbers
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))

print("Returned value from function:")
#calling the function to get the returned value
n1, n2 = swapN(n1, n2)
print("Number 1:",n1," Number 2: ",n2)

```

### Output

```bash
Enter Number 1: 2
Enter Number 2: 1
Returned value from function:
Number 1: 2  Number 2:  1
```

```bash
Enter Number 1: 1
Enter Number 2: 2
Returned value from function:
Number 1: 2  Number 2:  1
```

### Source Code
[Download Source Code](./p15.py ':ignore')
