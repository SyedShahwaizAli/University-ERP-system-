class User:
    def __init__(self, name, email, gender, user_id):
        self.name = name
        self.email = email
        self.gender = gender
        self.user_id = user_id

class Student(User):
    def __init__(self, name, email, gender, user_id, roll_no, semester):
        super().__init__(name, email, gender, user_id)
        self.roll_no = roll_no
        self.semester = semester
        self.enrolled_courses = []
        self.grades = {}
    
    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)
    
    def view_grades(self):
        print("\nGrades for %s:" % self.name)
        for course, grade in self.grades.items():
            print("%s: %s" % (course, grade))
    
    def generate_report(self):
        print("\nStudent Report for %s" % self.name)
        print("Roll No: %s" % self.roll_no)
        print("Semester: %s" % self.semester)
        print("Enrolled Courses:")
        for course in self.enrolled_courses:
            print("- %s" % course.title)
        self.view_grades()

class Teacher(User):
    def __init__(self, name, email, gender, user_id, employee_id, department):
        super().__init__(name, email, gender, user_id)
        self.employee_id = employee_id
        self.department = department
        self.assigned_courses = []
    
    def assign_grade(self, student, course, grade):
        if course in student.enrolled_courses:
            student.grades[course.title] = grade
            print("Grade %s assigned to %s in %s" % (grade, student.name, course.title))
        else:
            print("Error: %s is not enrolled in %s" % (student.name, course.title))
    
    def generate_report(self):
        print("\nTeacher Report for %s" % self.name)
        print("Employee ID: %s" % self.employee_id)
        print("Department: %s" % self.department)
        print("Assigned Courses:")
        for course in self.assigned_courses:
            print("- %s" % course.title)

class Course:
    def __init__(self, course_code, title, credit_hours):
        self.course_code = course_code
        self.title = title
        self.credit_hours = credit_hours
        self.teacher = None
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def assign_teacher(self, teacher):
        self.teacher = teacher
        teacher.assigned_courses.append(self)
    
    def show_summary(self):
        print("\nCourse Summary for %s" % self.title)
        print("Course Code: %s" % self.course_code)
        print("Credit Hours: %s" % self.credit_hours)
        teacher_name = self.teacher.name if self.teacher else 'Not Assigned'
        print("Teacher: %s" % teacher_name)
        print("Enrolled Students:")
        for student in self.students:
            print("- %s" % student.name)

class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.courses = []
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_course(self, course):
        self.courses.append(course)

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)
    
    def register_student(self, student, department):
        department.add_student(student)
    
    def hire_teacher(self, teacher, department):
        department.add_teacher(teacher)
    
    def enroll_student_in_course(self, student, course):
        student.enroll(course)

if __name__ == "__main__":
    my_uni = University("FAST University")
    cs_dept = Department("Computer Science")
    math_dept = Department("Mathematics")
    my_uni.add_department(cs_dept)
    my_uni.add_department(math_dept)
    
    t1 = Teacher("Ahmed Khan", "ahmed@uni.edu", "M", "T001", "EMP001", "Computer Science")
    t2 = Teacher("Zainab Ali", "zainab@uni.edu", "F", "T002", "EMP002", "Mathematics")
    
    s1 = Student("Ali Hassan", "ali@uni.edu", "M", "S001", "R001", 1)
    s2 = Student("Moiz Ahmed", "moiz@uni.edu", "M", "S002", "R002", 1)
    s3 = Student("Fatima Khan", "fatima@uni.edu", "F", "S003", "R003", 2)
    
    python = Course("CS101", "Python Programming", 3)
    java = Course("CS102", "Java Programming", 3)
    math = Course("MT101", "Basic Mathematics", 3)
    
    python.assign_teacher(t1)
    java.assign_teacher(t1)
    math.assign_teacher(t2)
    
    cs_dept.add_teacher(t1)
    math_dept.add_teacher(t2)
    cs_dept.add_course(python)
    cs_dept.add_course(java)
    math_dept.add_course(math)
    
    my_uni.enroll_student_in_course(s1, python)
    my_uni.enroll_student_in_course(s1, math)
    my_uni.enroll_student_in_course(s2, python)
    my_uni.enroll_student_in_course(s3, java)
    
    t1.assign_grade(s1, python, "A")
    t2.assign_grade(s1, math, "B")
    t1.assign_grade(s2, python, "A+")
    t1.assign_grade(s3, java, "B+")
    
    print("\nCOURSE SUMMARIES:")
    python.show_summary()
    java.show_summary()
    math.show_summary()
    
    print("\nGENERATING REPORTS:")
    for dept in my_uni.departments:
        for person in dept.teachers + dept.students:
            person.generate_report()