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
    def name(self, value: str):
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
