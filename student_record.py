students = [(101, "John", 85,20), (102, "Jane", 90,30), (103, "Jim", 78,18)]

max_grade = 0

for student_id, student_name, student_grade, student_age in students:
        if student_grade > max_grade:
            max_grade = student_grade
            top_student = (student_id, student_name, student_grade, student_age)

#top_student = max(students, key=lambda s: s[2]) #lambda is an anonymous function
print(top_student)

student_list = [(student_name,student_grade) for student in students]

print(student_list)







