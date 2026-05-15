students = []
def add_student(name):
    students.append(name)
def display_students():
    if len(students) == 0:
        print("No students available")
        return
    print("Students list:")
    for student in students:
        print(f"Student: {student}")
def search_student(name):
    # print("Present" if students.__contains__(name) == 1 else "Not Present") # Thechnically works but industry standard is
    print(f"Student: {name} Present" if name in students else f"Student: {name} is not Present") # Industry standard # Good Coding Practice # Readable
def remove_student(name):
    if name in students: 
        students.remove(name)
        print(f"Student removed : {name}")
    else: 
        print(f"Student not found to remove : {name}")    

add_student("Nagarjuna")
add_student("Mani")
display_students()
remove_student("Nagarjuna")
search_student("Mani Prakash")
display_students()