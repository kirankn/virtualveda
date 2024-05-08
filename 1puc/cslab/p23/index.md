## 23. Write a program to input names of n students and store them in a tuple. Also, input a name from the user and find if this student is present in the tuple or not.

<!-- ### Flowchart
![Image](./p23.png) -->

### Program
[Download Source Code](./p23.py ':ignore')
```python
#Creating user defined function
def searchStudent(tuple1,search):
    for a in tuple1:
        if(a == search):
            print("The name",search,"is present in the tuple")
            return
    print("The name",search,"is not found in the tuple")

name = tuple()

# Create empty tuple 'name' to store the values
n = int(input("How many names do you want to enter?: "))
for i in range(0,n):
    num = input("> ")
    #It will assign emailid entered by user to tuple 'name'
    name = name + (num,)

print("\nThe names entered in the tuple are:")
print(name)

# Asking the user to enter the name of the student to search
search = input("\nEnter the name of the student you want to search? ")

# Calling the search Student function
searchStudent(name,search)
```

### Output

```bash
How many names do you want to enter?: 4
> kkn
> vk
> avk
> adk

The names entered in the tuple are:
('kkn', 'vk', 'avk', 'adk')

Enter the name of the student you want to search? avk
The name avk is present in the tuple
```

```bash
How many names do you want to enter?: 4
> kkn
> vk
> avk
> adk

The names entered in the tuple are:
('kkn', 'vk', 'avk', 'adk')

Enter the name of the student you want to search? py
The name py is not found in the tuple
```