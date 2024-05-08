#Defining a function which takes name and gender as input
def prefix(name,gender):
    if (gender == 'M' or gender == 'm'):
        print("Hello, Mr.",name)
    elif (gender == 'F' or gender == 'f'):
        print("Hello, Ms.",name)
    else:
        print("Please enter only M or F in gender")

#Asking the user to enter the name
name = input("Enter your name: ")

#Asking the user to enter the gender as M/F
gender = input("Enter your gender: M/m for Male, and F/f for Female: ")

#calling the function
prefix(name,gender)
