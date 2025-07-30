students = ["Alice", "Bob", "Charlie", "David", "Eve"]
grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

print(list(enumerate(students, start=1)))

for i, (student, grade) in enumerate(zip(students, grades), start=1):
    print(f"Student {i}: {student} has a grade of {grade}")
    
high_scorerers = [student for student, grade in zip(students, grades) if grade > 95]


for i in range(len(students)):
    