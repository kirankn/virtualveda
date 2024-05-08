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
