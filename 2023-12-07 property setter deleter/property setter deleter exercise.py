class student:
    def __init__(
        self,
        school_address="None",
        school="None",
        major="None",
        chair="None",
        student="None",
        ID="None",
        personal_address="None",
        credit="None",
        gpa="None",
    ):
        self.school_address = school_address
        self.school = school
        self.major = major
        self.chair = chair
        self.student = student
        self.ID = ID
        self.personal_address = personal_address
        self.credit = credit
        self.gpa = gpa

    def __str__(self):
        return f"School_address: {self.school_address}\nSchool: {self.school}\nMajor: {self.major}\nChair: {self.chair}\nStudent: {self.student}\nID: {self.ID}\nPersonal_address: {self.personal_address}\nCredit: {self.credit}\nGPA: {self.gpa}"

    @property
    def student_name(self):
        print(f'"{self.student}" was accessed')
        return self.student

    @student_name.setter
    def student_name(self, value):
        print(f'"{self.student}" is now {value}')
        self.student = value

    @student_name.deleter
    def student_name(self):
        print(f'"{self.student}" was deleted')
        del self.student


if __name__ == "__main__":
    student_test = student(
        school_address="Tainan city yongkang district",
        school="STUST",
        major="CSE",
        chair="Gwo-Jiun Horng",
        student="Jason",
        ID="4B0G----",
        personal_address="Tainan city yongkang district",
        credit="97",
        gpa="4.1",
    )

    print(student_test.student)

    student_test.student_name = "Eric"
    del student_test.student_name
