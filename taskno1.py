
print('---------------------')
print("-Student Grade System-")
print("---------------------")

name=input("Enter student name:")
class1=int(input("Enter the name of class:"))

subject1=input("Enter the subject:")
subject2=input("Enter the subject:")
subject3=input("Enter the subject:")

marks1=int(input(f"Enter the marks of subject {subject1}:"))
marks2=int(input(f"Enter the marks of subject {subject2}:"))
marks3=int(input(f"Enter the marks of subject {subject3}:"))
avarage=(marks1+marks2+marks3)/3
print("The average marks of student is:",avarage)


if avarage>=90:
    print("Grade A")

elif avarage>=80 and avarage<90:
    print("Grade B")

elif avarage>=70 and avarage<80:
    print("Grade C")

elif avarage>=60 and avarage<70:
    print("Grade D")

elif avarage<=50:
    print("Grade F")
