import re

text = open('text.txt')

students_per_section = {}
students_per_course = {}
best_per_section = {}
best_overall_grade = None
best_overall_students = []

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

        course_match = re.search(r"[A-Z]+", section)
        course = course_match.group() if course_match else "UNKNOWN"

        # Count students per section
        if section not in students_per_section:
            students_per_section[section] = 1
        else:
            students_per_section[section] += 1

        # Count students per course
        if course not in students_per_course:
            students_per_course[course] = 1
        else:
            students_per_course[course] += 1

        # Highest grade per section (LOWEST grade value)
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

# -------------------------------
# OUTPUT
# -------------------------------
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