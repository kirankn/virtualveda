no_of_std = int(input("Enter number of students: "))  
result = {}  
for i in range(no_of_std):  
   print("Enter Details of student No.", i+1)  
   roll_no = int(input("Roll No: "))  
   std_name = input("Student Name: ")  
   marks = int(input("Marks: "))  
   result[roll_no] = [std_name, marks]    
print(result)  
# Display names of students who have got marks more than 75  
print("Students who got more than 75 marks are:")
for student in result:  
   if result[student][1] > 75:  
       print(result[student][0])
