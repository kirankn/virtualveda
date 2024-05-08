## 7. Write a program that prints maximum and minimum of five numbers entered by the user.

<!-- ### Flowchart
![Image](./p7.png) -->

### Program
[Download Source Code](./p7.py ':ignore')
```python
#Program to input five numbers and print largest and smallest numbers
smallest = 0
largest = 0
for a in range(0,5):
    x = int(input("Enter the number: "))
    if a == 0:
        smallest = largest = x
    if(x < smallest):
        smallest = x
    if(x > largest):
        largest = x
print("The smallest number is",smallest)
print("The largest number is ",largest)
```

### Output

```bash
Enter the number: 12
Enter the number: 20
Enter the number: 3
Enter the number: 40
Enter the number: 26
The smallest number is 3
The largest number is  40
```
