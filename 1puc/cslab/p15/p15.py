#defining a function to swap the numbers
def swapN(a, b):
    if(a < b):
        return b,a
    else:
        return a,b

#asking the user to provide two numbers
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))

print("Returned value from function:")
#calling the function to get the returned value
n1, n2 = swapN(n1, n2)
print("Number 1:",n1," Number 2: ",n2)
