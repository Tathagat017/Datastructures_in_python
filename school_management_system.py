
school_data = {
    "Math": {
        "teacher": "Ms. Johnson",
        "students": {
            "Alice": 92,
            "Bob": 85,
            "Charlie": 78,
            "Diana": 95
        }
    },
    "Science": {
        "teacher": "Mr. Smith",
        "students": {
            "Eve": 88,
            "Frank": 91,
            "Grace": 84,
            "Henry": 89
        }
    },
    "English": {
        "teacher": "Mrs. Brown",
        "students": {
            "Ivy": 96,
            "Jack": 82,
            "Kate": 87,
            "Liam": 93
        }
    },
    "History": {
        "teacher": "Dr. Wilson",
        "students": {
            "Mia": 90,
            "Noah": 79,
            "Olivia": 85,
            "Paul": 88
        }
    }
}

def print_teacher_names(school_data):
    """
    Task 1: Print Teacher Names
    Iterate through all classes and print the name of each teacher.
    """
    print("=== TEACHER NAMES ===")
    for class_name, class_info in school_data.items():
        teacher_name = class_info["teacher"]
        print(f"{class_name}: {teacher_name}")
    print()

def calculate_class_averages(school_data):
    """
    Task 2: Calculate Class Average Grades
    For each class, calculate and display the average grade of the students.
    """
    print("=== CLASS AVERAGE GRADES ===")
    class_averages = {}
    
    for class_name, class_info in school_data.items():
        students = class_info["students"]
        grades = list(students.values())
        average_grade = sum(grades) / len(grades)
        class_averages[class_name] = average_grade
        print(f"{class_name}: {average_grade:.2f}")
    
    print()
    return class_averages

def find_top_student(school_data):
    """
    Task 3: Find Top Student Across All Classes
    Identify the student with the highest grade among all students across every class.
    """
    print("=== TOP STUDENT ACROSS ALL CLASSES ===")
    top_student = None
    highest_grade = 0
    top_student_class = None
    
    for class_name, class_info in school_data.items():
        students = class_info["students"]
        for student_name, grade in students.items():
            if grade > highest_grade:
                highest_grade = grade
                top_student = student_name
                top_student_class = class_name
    
    print(f"Top Student: {top_student}")
    print(f"Grade: {highest_grade}")
    print(f"Class: {top_student_class}")
    print()
    
    return top_student, highest_grade, top_student_class

def demonstrate_tuple_unpacking(school_data):
    """
    Task 4: Use Unpacking
    Use tuple unpacking to extract and work with student names and grades separately.
    """
    print("=== TUPLE UNPACKING DEMONSTRATION ===")
    
    
    print("Method 1: Unpacking student items")
    for class_name, class_info in school_data.items():
        print(f"\n{class_name} students:")
        students = class_info["students"]
        for student_name, grade in students.items():
           
            student_info = (student_name, grade)
            name, score = student_info  
            print(f"  Student: {name}, Grade: {score}")
    
    print("\n" + "="*50)
    
   
    print("Method 2: Unpacking lists of names and grades")
    for class_name, class_info in school_data.items():
        students = class_info["students"]
  
        student_names = list(students.keys())
        student_grades = list(students.values())
        
        print(f"\n{class_name}:")
        print(f"  Names: {student_names}")
        print(f"  Grades: {student_grades}")
        
        # Demonstrate unpacking with zip
        print("  Using zip and unpacking:")
        for name, grade in zip(student_names, student_grades):
            print(f"    {name}: {grade}")
    
    print("\n" + "="*50)
    
    # Method 3: Advanced unpacking with multiple assignment
    print("Method 3: Advanced unpacking examples")
    
    # Get all students across all classes using unpacking
    all_students = []
    for class_name, class_info in school_data.items():
        students = class_info["students"]
        for student_data in students.items():
            name, grade = student_data  # Tuple unpacking
            all_students.append((name, grade, class_name))
    
    # Sort by grade (descending) and unpack top 3
    all_students.sort(key=lambda x: x[1], reverse=True)
    
    print("Top 3 students across all classes:")
    for i, (name, grade, class_name) in enumerate(all_students[:3], 1):
        print(f"  {i}. {name}: {grade} (from {class_name})")
    
    # Demonstrate unpacking with starred expressions
    print(f"\nUsing starred unpacking:")
    top_student, *other_top_students = all_students[:4]
    top_name, top_grade, top_class = top_student
    print(f"#1 Student: {top_name} with {top_grade} from {top_class}")
    print(f"Other top students: {len(other_top_students)} students")
    
    print()

def additional_analysis(school_data):
    """
    Additional analysis using the data structures
    """
    print("=== ADDITIONAL ANALYSIS ===")
    
    # Find class with highest average
    class_averages = {}
    for class_name, class_info in school_data.items():
        students = class_info["students"]
        grades = list(students.values())
        average_grade = sum(grades) / len(grades)
        class_averages[class_name] = average_grade
    
    best_class = max(class_averages, key=class_averages.get)
    best_average = class_averages[best_class]
    print(f"Class with highest average: {best_class} ({best_average:.2f})")
    
    # Count total students
    total_students = sum(len(class_info["students"]) for class_info in school_data.values())
    print(f"Total students in school: {total_students}")
    
    # Find students with grade above 90
    high_achievers = []
    for class_name, class_info in school_data.items():
        students = class_info["students"]
        for student_name, grade in students.items():
            if grade >= 90:
                high_achievers.append((student_name, grade, class_name))
    
    print(f"High achievers (90+ grade): {len(high_achievers)} students")
    for name, grade, class_name in high_achievers:
        print(f"  {name}: {grade} (from {class_name})")
    
    print()

def main():
    """
    Main function to run all tasks
    """
    print("SCHOOL MANAGEMENT SYSTEM")
    print("=" * 50)
    
    # Task 1: Print Teacher Names
    print_teacher_names(school_data)
    
    # Task 2: Calculate Class Average Grades
    calculate_class_averages(school_data)
    
    # Task 3: Find Top Student Across All Classes
    find_top_student(school_data)
    
    # Task 4: Use Unpacking
    demonstrate_tuple_unpacking(school_data)
    
    # Additional analysis
    additional_analysis(school_data)

if __name__ == "__main__":
    main()
