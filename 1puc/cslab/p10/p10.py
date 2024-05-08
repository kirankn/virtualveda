#Initializing the sum to zero
sum = 0
# Asking the user for input and storing it as a string
n = input("Enter the number: ")
# Looping through each digit of the string
# Converting it to int and then adding it to sum
for i in n:
    sum = sum + int(i)
# Printing the sum
print("The sum of digits of the number is",sum)
