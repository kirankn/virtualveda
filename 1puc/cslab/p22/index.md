## 22. Write a program to read email IDs of n number of students and store them in a tuple. Create two new tuples, one to store only the usernames from the email IDs and second to store domain names from the email IDs. Print all three tuples at the end of the program. [Hint: You may use the function split()]

<!-- ### Flowchart
![Image](./p22.png) -->

### Program
[Download Source Code](./p22.py ':ignore')
```python
emails = tuple()
username = tuple()
domainname = tuple()
#Create empty tuple 'emails', 'username' and domain-name
n = int(input("How many email ids you want to enter?: "))
for i in range(0,n):
    emid = input("> ")
    #It will assign emailid entered by user to tuple 'emails'
    emails = emails +(emid,)
    #This will split the email id into two parts, username and domain and return a list
    spl = emid.split("@")
    #assigning returned list first part to username and second part to domain name
    username = username + (spl[0],)
    domainname = domainname + (spl[1],)

# Printing the tuples
print("\nThe email ids in the tuple are:")
print(emails)

print("\nThe username in the email ids are:")
print(username)

print("\nThe domain name in the email ids are:")
print(domainname)
```

### Output

```bash
How many email ids you want to enter?: 3
> ramu@vet.com
> raju@sit.com
> subbu@nie.com

The email ids in the tuple are:
('ramu@vet.com', 'raju@sit.com', 'subbu@nie.com')

The username in the email ids are:
('ramu', 'raju', 'subbu')

The domain name in the email ids are:
('vet.com', 'sit.com', 'nie.com')
```