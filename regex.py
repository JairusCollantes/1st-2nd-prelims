import re

text = open('text.txt').readlines()

students_per_section = {}
students_per_course = {}
best_per_section = {}
best_overall_grade = None
best_overall_students = []

# ================================
# Use findall
# ================================
all_sections = re.findall(r"[A-Z]+-\d[A-Z]", "\n".join(text))
all_courses = [re.findall(r"[A-Z]+", sec)[0] for sec in all_sections]

# Count total students per section
for section in all_sections:
    if section not in students_per_section:
        students_per_section[section] = 1
    else:
        students_per_section[section] += 1

# Count total students per course
for course in all_courses:
    if course not in students_per_course:
        students_per_course[course] = 1
    else:
        students_per_course[course] += 1

# ================================
# Data processing
# ================================
for line in text:
    match = re.search(
        r"ID:\sA\d{2}-\d{4}\s"
        r"([A-Za-z]+\s[A-Za-z]+)\s"
        r"([A-Z]+-\d[A-Z])\s:\s"
        r"(\d+\.\d+)",
        line
    )

    if match:
        name = match.group(1)
        section = match.group(2)
        grade = float(match.group(3))

        # Highest grade per section
        if section not in best_per_section:
            best_per_section[section] = {
                "grade": grade,
                "students": [name]
            }
        else:
            if grade < best_per_section[section]["grade"]:
                best_per_section[section]["grade"] = grade
                best_per_section[section]["students"] = [name]
            elif grade == best_per_section[section]["grade"]:
                best_per_section[section]["students"].append(name)

        # Highest grade overall
        if best_overall_grade is None or grade < best_overall_grade:
            best_overall_grade = grade
            best_overall_students = [name]
        elif grade == best_overall_grade:
            best_overall_students.append(name)

# ================================
# OUTPUT
# ================================
print("===NUMBER OF STUDENTS PER SECTION===")
for section in students_per_section:
    print(section, ":", students_per_section[section])

print("\n===HIGHEST GRADE PER SECTION===")
for section in best_per_section:
    print(
        section,
        "- Grade:", best_per_section[section]["grade"],
        "| Students:", ", ".join(best_per_section[section]["students"])
    )

print("\n===HIGHEST GRADE OVERALL===")
print("Grade:", best_overall_grade)
print("Students:", ", ".join(best_overall_students))

print("\n===TOTAL STUDENTS PER COURSE===")
for course in students_per_course:
    print(course, ":", students_per_course[course])