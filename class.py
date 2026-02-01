#lock in na tlga
class Student():
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
    def get_student_id(self):
        return self._student_id
    
    def set_student_id(self, student_id):
        self._student_id = student_id   
        
    def enroll(self, course):
        pass
    
    def drop(self, course):
        pass
    
    def add_subject(self, course):
        pass
    
class Course():
    def __init__(self, course_name, course_code):
        self._course_name = course_name
        self._course_code = course_code
    
    def get_course_name(self):
        return self._course_name
    
    def set_course_name(self, course_name):
        self._course_name = course_name

class Section():
    def __init__(self, section_id, slot, schedule):
        self._section_id = section_id
        self._slot = slot
        self._schedule = schedule
    
    def get_section_id(self):
        return self._section_id
    
    def set_section_id(self, section_id):
        self._section_id = section_id

class Block():
    def __init__(self, block_name):
        self._block_name = block_name