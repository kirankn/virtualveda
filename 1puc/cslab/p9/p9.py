#Program to print the table of a number
num = int(input("Enter the number to display its multiplication table: "))
print("Multiplication Table: ");
for a in range(1,11):
    print(num," × ",a," = ",(num*a))
