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
