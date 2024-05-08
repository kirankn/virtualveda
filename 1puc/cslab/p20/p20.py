# Function to determine the largest number in a list
def largestNum(list1):
    length = len(list1)
    num = 0
    for i in range(length):
        if(i == 0 or list1[i] > num):
            num = list1[i]
    return num

list1 = [1, 2, 3, 4, 5, 6, 17, 8, 9]

# Using largestNum function to get the function
max_num = largestNum(list1)
# Printing all the elements for the list
print("The elements of the list",list1)
# Printing the largest num
print("\nThe largest number of the list:",max_num)
