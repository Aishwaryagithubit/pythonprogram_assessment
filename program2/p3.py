#ask user to enter number of students and required group size
students = int(input("How many students?"))
size = int(input("Required group size?"))
#Calculate the number of full groups and the leftover students
create_group = students//size
left_over = students % size 
print(f"There will be {create_group} groups with {left_over} students left over.")