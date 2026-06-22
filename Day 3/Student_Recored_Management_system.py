student=[]
def add_student():
    data={
        "name":input("Enter the name of student:"),
        "Roll Number":input("Enter the Roll Number of student:"),
        "Age":input("Enter the age of student:"),
        "Course":input("Enter the course of student:")

    }
    student.append(data)
    print("Student added Successfully")

def view_student():

    if len(student)==0:
        print("No student record found.")
    else:
        print("All Student Records")
        for s in student:
            print("------------------------------")
            print("Name:",s["name"])
            print("Roll Number:",s["Roll Number"])
            print("Age:",s["Age"])
            print("Course:",s["Course"])
    print("Total number of students:",len(student))

def find_student():
    roll_number=input("Enter the Roll number of student to find:")
    for s in student:
        if s["Roll Number"]==roll_number:
            print("Student found:")
            print("------------------------------")
            print("Name:",s["name"])
            print("Roll Number:",s["Roll Number"])
            print("Age:",s["Age"])
            print("Course:",s["Course"])
            return s
    return None

def  update_student():
    found_student=find_student()
    if found_student:
        print("Enter new details for the student:")
        found_student["name"]=input("Enter the name of student:")
        found_student["Roll Number"]=input("Enter the Roll Number of student:")
        found_student["Age"]=input("Enter the age of student:")
        found_student["Course"]=input("Enter the course of student:")
        print("Student record updated successfully.")
    else:
        print("No student record found to update.")
