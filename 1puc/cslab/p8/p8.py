#Program to print the grade of the student
n = float(input('Enter the percentage of the student: '))

if(n > 90):
    print("Grade A")
elif(n > 80):
    print("Grade B")
elif(n > 70):
    print("Grade C")
elif(n >= 60):
    print("Grade D")
else:
    print("Grade E")
