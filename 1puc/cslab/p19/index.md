## 19. Write a program to find the number of times an element occurs in the list.

<!-- ### Flowchart
![Image](./p19.png) -->

### Program
```python
#defining a list
list1 = [10, 20, 30, 40, 50, 60, 20, 50, 10, 30, 50, 30, 24, 45]

#printing the list for the user
print("The list is:", list1)

#asking the element to count
inp = int(input("Which element occurrence would you like to count? "))

#using the count function
count = list1.count(inp)

#printing the output
print("The count of element",inp,"in the list is:",count)
```

### Output

```bash
The list is: [10, 20, 30, 40, 50, 60, 20, 50, 10, 30, 50, 30, 24, 45]
Which element occurrence would you like to count? 50
The count of element 50 in the list is: 3
```
### Source Code
[Download Source Code](./p19.py ':ignore')
