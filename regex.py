import re

text = open('text.txt')

# ================================
# Data storage
# ================================
students = []
section_stats = {}  
course_stats = {} 

# Parse the data
for line in text:
    match = re.match(r'ID: (\S+) (\S+) (\S+) (\S+)-(\S+) : (\S+)', line)
    if match:
        student_id, first_name, last_name, course, section, grade = match.groups()
        full_name = f"{first_name} {last_name}"
        full_section = f"{course}-{section}"
        grade = float(grade)
        
        # Add to students list
        students.append({
            'id': student_id,
            'name': full_name,
            'course': course,
            'section': full_section,
            'grade': grade
        })
        
        # Update section stats
        if full_section not in section_stats:
            section_stats[full_section] = []
        section_stats[full_section].append((full_name, grade))
        
        # Update course stats
        if course not in course_stats:
            course_stats[course] = 0
        course_stats[course] += 1
