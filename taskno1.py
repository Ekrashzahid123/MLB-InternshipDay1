print('---------------------')
print("-Student Grade System-")
print("---------------------")
noofstudent=int(input("Enter the total number of students:"))
name=input("Enter student name:")
class1=int(input("Enter the name of class:"))
marks=int(input("Enter the marks of subject physics:"))


if(marks<0 or marks>100):
    print("Invalid marks. Please enter a value between 0 and 100.")


elif marks>90:
    print("Grade A")

elif marks>=80 and marks<90:
    print("Grade B")

elif marks>70 and marks<=80:
    print("Grade C")

elif marks>60 and marks<70:
    print("Grade D")

elif marks>50 and marks<=60:
    print("Grade F")
