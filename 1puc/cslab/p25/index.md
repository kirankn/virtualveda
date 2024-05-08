## 25. Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have marks above 75.

<!-- ### Flowchart
![Image](./p25.png) -->

### Program
```python
no_of_std = int(input("Enter number of students: "))  
result = {}  
for i in range(no_of_std):  
   print("Enter Details of student No.", i+1)  
   roll_no = int(input("Roll No: "))  
   std_name = input("Student Name: ")  
   marks = int(input("Marks: "))  
   result[roll_no] = [std_name, marks]    
print(result)  
# Display names of students who have got marks more than 75  
print("Students who got more than 75 marks are:")
for student in result:  
   if result[student][1] > 75:  
       print(result[student][0])
```

### Output

```bash
Enter number of students: 3
Enter Details of student No. 1
Roll No: 1
Student Name: Anil
Marks: 76
Enter Details of student No. 2
Roll No: 2
Student Name: Sunil
Marks: 75
Enter Details of student No. 3
Roll No: 3
Student Name: Rani
Marks: 82
{1: ['Anil', 76], 2: ['Sunil', 75], 3: ['Rani', 82]}
Students who got more than 75 marks are:
Anil
Rani
```
### Source Code
[Download Source Code](./p25.py ':ignore')
