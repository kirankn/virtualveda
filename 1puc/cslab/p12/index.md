## 12. Write a program to print the following pattern.
 1 2 3 4 5 <br>
 1 2 3 4 <br>
 1 2 3 <br>
 1 2 <br>
 1 <br>

<!-- ### Flowchart
![Image](./p12.png) -->

### Program
```python
n = 5
for i in range (n, 0, -1):
    # The space will increase on each iteration as i value will decrease
    space = (n - i)*" "
    #uncomment the below line if you wish to print as an inverted funnel
    #print(space, end=" ")
    #This for loop will print the increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

### Output

```bash
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
```
### Source Code
[Download Source Code](./p12.py ':ignore')
