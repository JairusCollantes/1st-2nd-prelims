#lock in na tlga
class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self._enrolled_block = None
        self._courses = []

    # Getters and Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def enrolled_block(self):
        return self._enrolled_block

    @enrolled_block.setter
    def enrolled_block(self, value):
        self._enrolled_block = value

    @property
    def courses(self):
        return self._courses.copy()

    @courses.setter
    def courses(self, value):
        self._courses = value
        
    # Methods
    # Enroll the student in a block
    def enroll_block(self, block):
        self._enrolled_block = block
    
    # Drop a course from the student's course list
    def drop(self, course):
        if course in self._courses:
            self._courses.remove(course)
    # Add a course to the student's course list
    def add_subject(self, course):
        if course not in self._courses:
            self._courses.append(course)
    
    # Get courses from the enrolled block
    def get_block_courses(self):
        if self._enrolled_block:
            return self._enrolled_block.courses
        return []
    
class Course:
    def __init__(self, course_name, course_code):
        self._course_name = course_name
        self._course_code = course_code

    # Getters and Setters
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value

    @property
    def course_code(self):
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        self._course_code = value

class Section:
    def __init__(self, section_id, slot, schedule):
        self._section_id = section_id
        self._slot = slot
        self._schedule = schedule
        self._block = None
        self._students_enrolled = []

    # Getters and Setters
    @property
    def section_id(self):
        return self._section_id

    @section_id.setter
    def section_id(self, value):
        self._section_id = value

    @property
    def slot(self):
        return self._slot

    @slot.setter
    def slot(self, value):
        self._slot = value

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, value):
        self._block = value

    @property
    def students_enrolled(self):
        return self._students_enrolled.copy()
    
    # Methods
    # Enroll a student in the section
    def enroll_student(self, student):
        if student not in self._students_enrolled:
            self._students_enrolled.append(student)
    
    # Drop a student from the section
    def drop_student(self, student):
        if student in self._students_enrolled:
            self._students_enrolled.remove(student)

class Block:
    def __init__(self, block_name):
        self._block_name = block_name
        self._courses = []

    # Getters and Setters
    @property
    def block_name(self):
        return self._block_name

    @block_name.setter
    def block_name(self, value):
        self._block_name = value

    @property
    def courses(self):
        return self._courses.copy()
    
    # Methods
    # Add a course to the block
    def add_course(self, course):
        if course not in self._courses:
            self._courses.append(course)
    
    # Remove a course from the block
    def remove_course(self, course):
        if course in self._courses:
            self._courses.remove(course)
            
students = []
courses = []
sections = []
blocks = []
while True:
    print("=========================================================")
    print("Welcome to the Student Management System")
    print("1. Manage Students")
    print("2. Manage Courses")
    print("3. Manage Sections")
    print("4. Manage Blocks")
    print("5. Exit")
    print("=========================================================")
    choice = input("Enter your choice: ")
    if choice == '5':
        print("Exiting the system. Goodbye!")
        break
    if choice == '1':
        print("Student management selected.")
        while True:
            print("=========================================================")
            print("1. Add Student")
            print("2. View Students")
            print("3. Add student to Block")
            print("4. Enroll student to course")
            print("5. Drop student from course")
            print("6. Back to Main Menu")
            print("=========================================================")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '6':
                break
            elif sub_choice == '1':
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                students.append(Student(name, student_id))
                print(f"Student {name} with ID {student_id} added.")
            elif sub_choice == '2':
                print("List of Students:")
                for student in students:
                    print(f"Name: {student.name}, ID: {student.student_id}")
            elif sub_choice == '3':
                print("List of Sections:")
                for section in sections:
                    print(f"ID: {section.section_id}, Slot: {section.slot}, Schedule: {section.schedule}")
                print("List of Students:")
                for student in students:
                    print(f"ID: {student.student_id}, Name: {student.name}")
                print("Add student to Section selected.")
                section_id = input("Enter section ID: ")
                student_id = input("Enter student ID to add: ")
                section = next((s for s in sections if s.section_id == section_id), None)
                student = next((st for st in students if st.student_id == student_id), None)
                if section and student:
                    section.enroll_student(student)
                    print(f"Student {student.name} added to Section {section.section_id}.")
                else:
                    print("Section or Student not found.")
            elif sub_choice == '4':
                print("List of Students:")
                for student in students:
                    print(f"ID: {student.student_id}, Name: {student.name}")
                print("List of Courses:")
                for course in courses:
                    print(f"Name: {course.course_name}, Code: {course.course_code}")
                print("Enroll student to course selected.")
                student_id = input("Enter student ID to enroll: ")
                course_code = input("Enter course code to enroll in: ")
                student = next((s for s in students if s.student_id == student_id), None)
                course = next((c for c in courses if c.course_code == course_code), None)
                if student and course:
                    student.enroll_course(course)
                    print(f"Student {student.name} enrolled in Course {course.course_name}.")
                else:
                    print("Student or Course not found.")
            elif sub_choice == '5':
                print("List of Students:")
                for student in students:
                    print(f"ID: {student.student_id}, Name: {student.name}")
                print("List of Courses:")
                for course in courses:
                    print(f"Name: {course.course_name}, Code: {course.course_code}")
                print("Drop student from course selected.")
                student_id = input("Enter student ID to drop from course: ")
                course_code = input("Enter course code to drop: ")
                student = next((s for s in students if s.student_id == student_id), None)
                course = next((c for c in courses if c.course_code == course_code), None)
                if student and course:
                    student.drop(course)
                    print(f"Student {student.name} dropped from Course {course.course_name}.")
                else:
                    print("Student or Course not found.")
    elif choice == '2':
        print("Course management selected.")
        while True:
            print("=========================================================")
            print("1. Add Course")
            print("2. View Courses")
            print("3. Back to Main Menu")
            print("=========================================================")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '3':
                break
            elif sub_choice == '1':
                course_name = input("Enter course name: ")
                course_code = input("Enter course code: ")
                course = Course(course_name, course_code)
                courses.append(course)
                print(f"Course {course_name} with code {course_code} added.")
            elif sub_choice == '2':
                print("List of Courses:")
                for course in courses:
                    print(f"Name: {course.course_name}, Code: {course.course_code}")
    elif choice == '3':
        print("Section management selected.")
        while True:
            print("=========================================================")
            print("1. Add Section")
            print("2. View Sections")
            print("3. Back to Main Menu")
            print("=========================================================")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '3':
                break
            elif sub_choice == '1':
                section_id = input("Enter section ID: ")
                slot = input("Enter slot: ")
                schedule = input("Enter schedule: ")
                section = Section(section_id, slot, schedule)
                sections.append(section)
                print(f"Section {section_id} added.")
            elif sub_choice == '2':
                print("List of Sections:")
                for section in sections:
                    print(f"ID: {section.section_id}, Slot: {section.slot}, Schedule: {section.schedule}")
    elif choice == '4':
        print("Block management selected.")
        while True:
            print("=========================================================")
            print("1. Add Block")
            print("2. View Blocks")
            print("3. Add course to Block")
            print("4. Assign Block to Section")
            print("5. Back to Main Menu")
            print("=========================================================")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '5':
                break
            elif sub_choice == '1':
                block_name = input("Enter block name: ")
                block = Block(block_name)
                blocks.append(block)
                print(f"Block {block_name} added.")
            elif sub_choice == '2':
                print("List of Blocks:")
                for block in blocks:
                    print(f"Block Name: {block.block_name}, Courses: {[course.course_name for course in block.courses]}")
            elif choice == '3':
                print("List of Blocks:")
                for block in blocks:
                    print(f"Block Name: {block.block_name}, Courses: {[course.course_name for course in block.courses]}")
                print("Add course to Block selected.")
                block_name = input("Enter block name: ")
                course_code = input("Enter course code to add: ")
                block = next((b for b in blocks if b.block_name == block_name), None)
                course = next((c for c in courses if c.course_code == course_code), None)
                if block and course:
                    block.add_course(course)
                    print(f"Course {course.course_name} added to Block {block.block_name}.")
                else:
                   print("Block or Course not found.")
            elif choice == '6':
                print("List of Sections:")
                for section in sections:
                    print(f"ID: {section.section_id}, Slot: {section.slot}, Schedule: {section.schedule}")
                print("Assign Block to Section selected.")
                section_id = input("Enter section ID: ")
                block_name = input("Enter block name to assign: ")
                section = next((s for s in sections if s.section_id == section_id), None)
                block = next((b for b in blocks if b.block_name == block_name), None)
                if section and block:
                    section.block = block
                    print(f"Block {block.block_name} assigned to Section {section.section_id}.")
                else:
                    print("Section or Block not found.")
    else:
        print("Invalid choice. Please try again.")
    