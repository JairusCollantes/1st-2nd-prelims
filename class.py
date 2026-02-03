# ================================
# Classes
# ================================
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
        combined_courses = self.get_block_courses() + self._courses
        # Remove duplicates by course_code
        unique_courses = []
        codes = []
        for c in combined_courses:
            if c.course_code not in codes:
                unique_courses.append(c)
                codes.append(c.course_code)
        return unique_courses

    # Methods
    def enroll_block(self, block):
        self._enrolled_block = block

    def add_subject(self, course):
        if course not in self._courses:
            self._courses.append(course)

    def drop(self, course):
        if course in self._courses:
            self._courses.remove(course)

    def get_block_courses(self):
        if self._enrolled_block:
            return self._enrolled_block.courses.copy()
        return []

class Course:
    def __init__(self, course_name, course_code):
        self._course_name = course_name
        self._course_code = course_code

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

class Block:
    def __init__(self, block_name):
        self._block_name = block_name
        self._courses = []

    @property
    def block_name(self):
        return self._block_name

    @block_name.setter
    def block_name(self, value):
        self._block_name = value

    @property
    def courses(self):
        return self._courses.copy()

    def add_course(self, course):
        if course not in self._courses:
            self._courses.append(course)

    def remove_course(self, course):
        if course in self._courses:
            self._courses.remove(course)

class Section:
    def __init__(self, section_id, slot, schedule):
        self._section_id = section_id
        self._slot = slot
        self._schedule = schedule
        self._block = None
        self._students_enrolled = []

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

    def enroll_student(self, student):
        if student not in self._students_enrolled:
            self._students_enrolled.append(student)
            if self._block:
                student.enroll_block(self._block)

    def drop_student(self, student):
        if student in self._students_enrolled:
            self._students_enrolled.remove(student)

# ================================
# Data storage
# ================================
students = []
courses = []
blocks = []
sections = []

# ================================
# Main Menu
# ================================
while True:
    print("\n==================== Student Management System ====================")
    print("1. Manage Students")
    print("2. Manage Courses")
    print("3. Manage Sections")
    print("4. Manage Blocks")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting the system. Goodbye!")
        break

    # -----------------------------
    # Student Management
    # -----------------------------
    elif choice == '1':
        while True:
            print("\n--- Student Menu ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Add student to Block")
            print("4. Enroll student to Course")
            print("5. Drop student from Course")
            print("6. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '6':
                break
            elif sub_choice == '1':
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                exists = False
                for s in students:
                    if s.student_id == student_id:
                        exists = True
                        break
                if exists:
                    print("Student ID already exists!")
                else:
                    students.append(Student(name, student_id))
                    print(f"Student {name} ({student_id}) added.")
            elif sub_choice == '2':
                if not students:
                    print("No students yet.")
                    continue
                for student in students:
                    course_list = [c.course_name for c in student.courses]
                    print(f"ID: {student.student_id}, Name: {student.name}, Courses: {course_list}")
            elif sub_choice == '3':
                student_id = input("Enter student ID: ")
                block_name = input("Enter block name: ")

                student = None
                for s in students:
                    if s.student_id == student_id:
                        student = s
                        break

                block = None
                for b in blocks:
                    if b.block_name == block_name:
                        block = b
                        break

                if student and block:
                    student.enroll_block(block)
                    print(f"Student {student.name} enrolled in Block {block.block_name}.")
                else:
                    print("Student or Block not found.")
            elif sub_choice == '4':
                student_id = input("Enter student ID: ")
                course_code = input("Enter course code: ")

                student = None
                for s in students:
                    if s.student_id == student_id:
                        student = s
                        break

                course = None
                for c in courses:
                    if c.course_code == course_code:
                        course = c
                        break

                if student and course:
                    student.add_subject(course)
                    print(f"Student {student.name} enrolled in Course {course.course_name}.")
                else:
                    print("Student or Course not found.")
            elif sub_choice == '5':
                student_id = input("Enter student ID: ")
                course_code = input("Enter course code: ")

                student = None
                for s in students:
                    if s.student_id == student_id:
                        student = s
                        break

                course = None
                for c in courses:
                    if c.course_code == course_code:
                        course = c
                        break

                if student and course:
                    student.drop(course)
                    print(f"Student {student.name} dropped Course {course.course_name}.")
                else:
                    print("Student or Course not found.")

    # -----------------------------
    # Course Management
    # -----------------------------
    elif choice == '2':
        while True:
            print("\n--- Course Menu ---")
            print("1. Add Course")
            print("2. View Courses")
            print("3. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '3':
                break
            elif sub_choice == '1':
                course_name = input("Enter course name: ")
                course_code = input("Enter course code: ")
                exists = False
                for c in courses:
                    if c.course_code == course_code:
                        exists = True
                        break
                if exists:
                    print("Course code already exists!")
                else:
                    courses.append(Course(course_name, course_code))
                    print(f"Course {course_name} ({course_code}) added.")
            elif sub_choice == '2':
                if not courses:
                    print("No courses yet.")
                    continue
                for course in courses:
                    print(f"Name: {course.course_name}, Code: {course.course_code}")

    # -----------------------------
    # Section Management
    # -----------------------------
    elif choice == '3':
        while True:
            print("\n--- Section Menu ---")
            print("1. Add Section")
            print("2. View Sections")
            print("3. Enroll Student to Section")
            print("4. Drop Student from Section")
            print("5. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '5':
                break
            elif sub_choice == '1':
                section_id = input("Enter section ID: ")
                slot = input("Enter slot: ")
                schedule = input("Enter schedule: ")

                exists = False
                for s in sections:
                    if s.section_id == section_id:
                        exists = True
                        break
                if exists:
                    print("Section ID already exists!")
                else:
                    sections.append(Section(section_id, slot, schedule))
                    print(f"Section {section_id} added.")
            elif sub_choice == '2':
                if not sections:
                    print("No sections yet.")
                    continue
                for section in sections:
                    block_name = section.block.block_name if section.block else "None"
                    students_list = [s.name for s in section.students_enrolled]
                    print(f"ID: {section.section_id}, Slot: {section.slot}, Schedule: {section.schedule}, Block: {block_name}, Students: {students_list}")
            elif sub_choice == '3':
                section_id = input("Enter section ID: ")
                student_id = input("Enter student ID: ")

                section = None
                for s in sections:
                    if s.section_id == section_id:
                        section = s
                        break

                student = None
                for st in students:
                    if st.student_id == student_id:
                        student = st
                        break

                if section and student:
                    section.enroll_student(student)
                    print(f"Student {student.name} enrolled in Section {section.section_id}.")
                else:
                    print("Section or Student not found.")
            elif sub_choice == '4':
                section_id = input("Enter section ID: ")
                student_id = input("Enter student ID: ")

                section = None
                for s in sections:
                    if s.section_id == section_id:
                        section = s
                        break

                student = None
                for st in students:
                    if st.student_id == student_id:
                        student = st
                        break

                if section and student:
                    section.drop_student(student)
                    print(f"Student {student.name} dropped from Section {section.section_id}.")
                else:
                    print("Section or Student not found.")

    # -----------------------------
    # Block Management
    # -----------------------------
    elif choice == '4':
        while True:
            print("\n--- Block Menu ---")
            print("1. Add Block")
            print("2. View Blocks")
            print("3. Add Course to Block")
            print("4. Assign Block to Section")
            print("5. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '5':
                break
            elif sub_choice == '1':
                block_name = input("Enter block name: ")
                exists = False
                for b in blocks:
                    if b.block_name == block_name:
                        exists = True
                        break
                if exists:
                    print("Block already exists!")
                else:
                    blocks.append(Block(block_name))
                    print(f"Block {block_name} added.")
            elif sub_choice == '2':
                if not blocks:
                    print("No blocks yet.")
                    continue
                for block in blocks:
                    course_list = [c.course_name for c in block.courses]
                    print(f"Block: {block.block_name}, Courses: {course_list}")
            elif sub_choice == '3':
                block_name = input("Enter block name: ")
                course_code = input("Enter course code to add: ")

                block = None
                for b in blocks:
                    if b.block_name == block_name:
                        block = b
                        break

                course = None
                for c in courses:
                    if c.course_code == course_code:
                        course = c
                        break

                if block and course:
                    block.add_course(course)
                    print(f"Course {course.course_name} added to Block {block.block_name}.")
                else:
                    print("Block or Course not found.")
            elif sub_choice == '4':
                section_id = input("Enter section ID: ")
                block_name = input("Enter block name to assign: ")

                section = None
                for s in sections:
                    if s.section_id == section_id:
                        section = s
                        break

                block = None
                for b in blocks:
                    if b.block_name == block_name:
                        block = b
                        break

                if section and block:
                    section.block = block
                    print(f"Block {block.block_name} assigned to Section {section.section_id}.")
                else:
                    print("Section or Block not found.")
    else:
        print("Invalid choice. Please try again.")