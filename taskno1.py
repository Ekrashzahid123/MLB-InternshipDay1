print('---------------------')
print("Student Grade System")
print("---------------------")
name=input("Enter student name:")
class1=int(input("Enter the name of class:"))
marks=int(input("Enter the marks of subject physics:"))

if marks>90:
    print("Grade A")

elif marks>=80 and marks<=90:
    print("Grade B")

elif marks>70 and marks<80:
    print("Grade C")

elif marks>60 and marks<70:
    print("Grade D")

else:
    print("Grade F")
