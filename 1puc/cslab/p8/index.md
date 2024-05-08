## 8. Write a program to find the grade of a student when grades are allocated as given in the table below. Percentage of the marks obtained by the student is input to the program.
| Percentage of Marks | Grade |
|---------------------|-------|
| Above  90%          | A     |
| 80% to 90%          | B     |
| 70% to 80%          | C     |
| 60% to 70%          | D     |
| Below 60%           | E     |

<!-- ### Flowchart
![Image](./p8.png) -->

### Program
[Download Source Code](./p8.py ':ignore')
```python
#Program to print the grade of the student
n = float(input('Enter the percentage of the student: '))

if(n > 90):
    print("Grade A")
elif(n > 80):
    print("Grade B")
elif(n > 70):
    print("Grade C")
elif(n >= 60):
    print("Grade D")
else:
    print("Grade E")
```

### Output

```bash
Enter the percentage of the student: 91
Grade A
```

```bash
Enter the percentage of the student: 72
Grade C
```