class Student:
    def __init__(
        self,
        student_name=None,
        student_identify_code=None,
        student_major=None,
        student_email=None,
        student_course=None,
        student_health=None,
    ):
        self.student_name = student_name
        self.student_identify_code = student_identify_code
        self.student_major = student_major
        self.student_email = student_email
        self.student_course = student_course
        self.student_health = student_health

    def __str__(self) -> str:
        return f"Student INFO:\nName: {self.student_name}\nID: {self.student_identify_code}\nMajor: {self.student_major}\nEmail: {self.student_email}\nCourse: {self.student_course}\nHealth: {self.student_health}"

    def Student_registration(
        self,
        name=None,
        identify_code=None,
        major=None,
        email=None,
        health=None,
    ):
        self.student_name = input("What is your name? ")
        self.student_identify_code = input("What is your identify code? ")
        self.student_major = input("What is your major? ")
        self.student_email = input("What is your email? ")
        self.student_health = input("How is your health? ")

    def Student_check_course(self):
        if self.student_course != None:
            print(f"Now your course is '{self.student_course}'!")
        else:
            print("You don't have any courses now!")

    def student_add_course(self):
        if self.student_course != None:
            print(
                f"You have a '{self.student_course}' course already, please withdraw first!"
            )
        else:
            self.student_course = input(f"Which course? ")
            if self.student_course != None:
                print("Add successfully!")
            else:
                print("Error, please retry!")

    def student_withdraw_course(self):
        if self.student_course != None:
            status = input("Are you sure you want to withdraw this course? (Y/N)")
            if status.lower() == "y":
                self.student_course = None
                print("Course withdraw success!")
            elif status.lower() == "n":
                print("Course withdraw canceled!")
            else:
                print("Wrong answer!")
        else:
            print("You don't have any courses now!")


s1 = Student()
s1.Student_registration()
print(s1)


s1.Student_check_course()
s1.student_add_course()
s1.Student_check_course()
s1.student_withdraw_course()
s1.Student_check_course()
