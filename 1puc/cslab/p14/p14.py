# Defining the function which will calculate the discriminant
def discriminant(a, b, c):
    d = b**2 - 4 * a * c
    return d

# Asking the user to provide values of a, b, and c
print("For a quadratic equation in the form of ax^2 + bx + c = 0")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
#Calling the function to get the discriminant
det = discriminant(a,b,c)
# Printing the result based on the discriminant value
if (det > 0):
    print("The quadratic equation has two real roots.")
elif (det == 0):
    print("The quadratic equation has one real root.")
else:
    print("The quadratic equation doesn't have any real root.")
