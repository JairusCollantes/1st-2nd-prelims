import random

first_names = [
    "John", "Maria", "Alex", "Chris", "Anna", "Mark", "Sophia",
    "Daniel", "Abzier", "Jervey", "Liam", "Nicole", "Glairoz", "Ella",
    "Jairus", "Vhinch", "Carlkirson", "Nash", "Gelo", "Owen", "Ava"
]

last_names = [
    "Cruz", "Reyes", "Santos", "Garcia", "Lopez", "Torres",
    "Flores", "Mendoza", "Ramos", "Aquino", "Punay", "Bolado", "Erezo",
    "Calusin", "Collantes", "Lambaco", "Sanchez", "Gabertan", "Razalan",
    "Solina", "Salvatierra"
]

courses = ["BSCS-1A", "BSIT-1A", "BSEMC-1A", "BSCS-1B", "BSIT-1B", "BSEMC-1B"]

used_ids = set()

def generate_unique_id():
    while True:
        number_part = random.randint(1000, 9999)
        student_id = f"A25-{number_part}"
        if student_id not in used_ids:
            used_ids.add(student_id)
            return student_id

with open("text.txt", "w") as file:
    for _ in range(1000):
        student_id = generate_unique_id()
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        course = random.choice(courses)
        grade = round(random.uniform(1.00, 1.75), 2)

        file.write(
            f"ID: {student_id} {name} {course} : {grade}\n"
        )