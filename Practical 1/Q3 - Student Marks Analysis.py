students=[]
n=int(input("Enter number of students: "))
subs=int(input("Enter number of subjects: "))
subNames=[input(f"Enter Name of Subject {i}: ") for i in range(1,subs+1)]

def inp_student(num):
    print(f"Enter Records for Student {num}.")
    name=input(("Student name: "))
    student=[name]
    for i in range(subs):
        marks=int(input(f"{subNames[i]} Marks: "))
        student.append(marks)
    avg=round(sum(student[1:])/subs,2)
    student.append(avg)
    return student    

#Taking input
for i in range(1,n+1):
    students.append(inp_student(i))
    
print(students)
print(f"Overall Topper: {max(students,key=lambda x:x[subs-1])[0]}")
for i in range(1,subs+1):
    print(f"{subNames[i-1]} topper: {max(students,key=lambda x:x[i])[0]}")
    

    
    