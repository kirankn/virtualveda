## 9. Write a function to print the table of a given number. The number has to be entered by the user.

<!-- ### Flowchart
![Image](./p9.png) -->

### Program
```python
#Program to print the table of a number
num = int(input("Enter the number to display its multiplication table: "))
print("Multiplication Table: ");
for a in range(1,11):
    print(num," × ",a," = ",(num*a))
```

### Output

```bash
Enter the number to display its multiplication table: 5
Multiplication Table: 
5  ×  1  =  5
5  ×  2  =  10
5  ×  3  =  15
5  ×  4  =  20
5  ×  5  =  25
5  ×  6  =  30
5  ×  7  =  35
5  ×  8  =  40
5  ×  9  =  45
5  ×  10  =  50
```
### Source Code
[Download Source Code](./p9.py ':ignore')
