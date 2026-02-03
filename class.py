# ================================
# Classes
# ================================
class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self._enrolled_block = None
        self._sections = []

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
    def sections(self):
        return self._sections.copy()
    
    # Methods
    def enroll_block(self, block):
        self.enrolled_block = block
        for section in block.sections:
            if section not in self._sections:
                self._sections.append(section)
                section.enroll_student(self)
    
    def add_section(self, section):
        if section not in self._sections:
            self._sections.append(section)
            section.enroll_student(self)
            
    def drop_section(self, section):
        if section in self._sections:
            self._sections.remove(section)
            section.drop_student(self)
    
    def list_courses(self):
        return [section.course_name for section in self._sections]  

class Block:
    def __init__(self, block_name):
        self._block_name = block_name
        self._sections = []

    @property
    def block_name(self):
        return self._block_name

    @block_name.setter
    def block_name(self, value):
        self._block_name = value

    @property
    def sections(self):
        return self._sections.copy()

    def add_section(self, section):
        if section not in self._sections:
            self._sections.append(section)
            section.block = self

    def remove_section(self, section):
        if section in self._sections:
            for student in section.students_enrolled:
                student.drop(section)
            
            self._sections.remove(section)
            section.block = None

class Section:
    def __init__(self, section_id, course_name , slot, schedule):
        self._section_id = section_id
        self._course_name = course_name 
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
    def course_name(self):
        return self._course_name
    
    @course_name.setter
    def course_name(self, value):
        self._course_name = value

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
            # if self._block:
            #     student.enroll_block(self._block)

    def drop_student(self, student):
        if student in self._students_enrolled:
            self._students_enrolled.remove(student)

# ================================
# Data storage
# ================================
students = []
blocks = []
sections = []

# ================================
# Main Menu
# ================================
while True:
    print("\n==================== Student Management System ====================")
    print("1. Manage Students")
    print("2. Manage Sections")
    print("3. Manage Blocks")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '4':
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
            print("4. Enroll student to Section")
            print("5. Drop student from Section")
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
                    course_list = student.list_courses()
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
                course_code = input("Enter section ID: ")
                
                student = None
                for s in students:
                    if s.student_id == student_id:
                        student = s
                        break

                section = None
                for c in sections:
                    if c.section_id == course_code:
                        section = c
                        break

                if student and section:
                    student.add_section(section)
                    print(f"Student {student.name} enrolled in Section {section.section_id}.")
                else:
                    print("Student or Section not found.")
            elif sub_choice == '5':
                student_id = input("Enter student ID: ")
                course_code = input("Enter section ID: ")

                student = None
                for s in students:
                    if s.student_id == student_id:
                        student = s
                        break

                section = None
                for c in sections:
                    if c.section_id == course_code:
                        section = c
                        break

                if student and section:
                    student.drop_section(section)
                    print(f"Student {student.name} dropped Section {section.section_id}.")
                else:
                    print("Student or Section not found.")
    # -----------------------------
    # Section Management
    # -----------------------------
    elif choice == '2':
        while True:
            print("\n--- Section Menu ---")
            print("1. Add Section")
            print("2. View Sections")
            print("3. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '3':
                break
            elif sub_choice == '1':
                section_id = input("Enter section ID: ")
                course_name = input("Enter course name: ")
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
                    sections.append(Section(section_id, course_name, slot, schedule))
                    print(f"Section {section_id} added.")
            elif sub_choice == '2':
                if not sections:
                    print("No sections yet.")
                    continue
                for section in sections:
                    block_name = section.block.block_name if section.block else "None"
                    students_list = [s.name for s in section.students_enrolled]
                    print(f"ID: {section.section_id}, Course: {section.course_name}, Slot: {section.slot}, Schedule: {section.schedule}, Block: {block_name}, Students: {students_list}")
    # -----------------------------
    # Block Management
    # -----------------------------
    elif choice == '3':
        while True:
            print("\n--- Block Menu ---")
            print("1. Add Block")
            print("2. View Blocks")
            print("3. Add Section to Block")
            print("4. Remove Section from Block")
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
                    course_list = [c.section_id for c in block.sections]
                    print(f"Block: {block.block_name}, Sections: {course_list}")
            elif sub_choice == '3':
                block_name = input("Enter block name: ")
                section_id = input("Enter section ID to add: ")
                block = None
                for b in blocks:
                    if b.block_name == block_name:
                        block = b
                        break

                section = None
                for c in sections:
                    if c.section_id == section_id:
                        section = c
                        break

                if block and section:
                    block.add_section(section)
                    print(f"Section {section.section_id} added to Block {block.block_name}.")
                else:
                    print("Block or Section not found.")
            elif sub_choice == '4':
                section_id = input("Enter section ID: ")
                block_name = input("Enter block name to remove section from: ")

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
                    block.remove_section(section)
                    print(f"Section {section.section_id} removed from Block {block.block_name}.")
                else:
                    print("Section or Block not found.")
    else:
        print("Invalid choice. Please try again.")