#Student Managment Module
def add_student():
    print("\n---Add Student---")
    name=input("Enter student name:")
    roll_no=input("Enter roll number:")
    course=input("Enter course:")
    student={"name":name,"roll_no":roll_no,"course":course}
    return student