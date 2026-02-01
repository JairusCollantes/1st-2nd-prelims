#lock in na tlga
class Student():
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id

class Course():
    def __init__(self, course_name, course_code):
        self._course_name = course_name
        self._course_code = course_code

class Section():
    def __init__(self, section_id, slot, schedule):
        self._section_id = section_id
        self._slot = slot
        self._schedule = schedule

class Block():
    def __init__(self, block_name):
        self._block_name = block_name