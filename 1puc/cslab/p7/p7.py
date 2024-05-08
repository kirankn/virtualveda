#Program to input five numbers and print largest and smallest numbers
smallest = 0
largest = 0
for a in range(0,5):
    x = int(input("Enter the number: "))
    if a == 0:
        smallest = largest = x
    if(x < smallest):
        smallest = x
    if(x > largest):
        largest = x
print("The smallest number is",smallest)
print("The largest number is ",largest)
