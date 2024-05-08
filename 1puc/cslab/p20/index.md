## 20. Write a program that returns the largest element of the element list passed as parameter.


<!-- ### Flowchart
![Image](./p20.png) -->

### Program
[Download Source Code](./p20.py ':ignore')
```python
# Function to determine the largest number in a list
def largestNum(list1):
    length = len(list1)
    num = 0
    for i in range(length):
        if(i == 0 or list1[i] > num):
            num = list1[i]
    return num

list1 = [1, 2, 3, 4, 5, 6, 17, 8, 9]

# Using largestNum function to get the function
max_num = largestNum(list1)
# Printing all the elements for the list
print("The elements of the list",list1)
# Printing the largest num
print("\nThe largest number of the list:",max_num)
```

### Output

```bash
The elements of the list [1, 2, 3, 4, 5, 6, 17, 8, 9]
The largest number of the list: 17
```

```bash
The elements of the list [1, 2, 3, 4, 5, 6, 7, 8, 9]
The largest number of the list: 9
```