# Given the list grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91], perform the following operations:

# Slice grades from index 2 to 7
# Use list comprehension to find grades above 85
# Replace the grade at index 3 with 95
# Append three new grades
# Sort in descending order and display the top 5 grades

list_grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced_grades = list_grades[2:8:1]

print(f"Sliced grades from index 2 to 7: {sliced_grades}")

grade_above_85 = [grade for grade in list_grades if grade>85]

for i in range(3):
    list_grades.append(i)
   
 # sorting the list in descending order   
list_grades = sorted(list_grades, reverse=True)
print(f"sosorted grades in descending order: {list_grades}")