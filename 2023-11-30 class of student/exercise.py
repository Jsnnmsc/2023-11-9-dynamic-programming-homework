class Student:
    def __init__(
        self,
        school_address="None",
        school="None",
        department="None",
        manager="None",
        student="None",
        ID="None",
        personal_address="None",
        credit="None",
        gpa="None",
    ):
        self.school_address = school_address
        self.school = school
        self.department = department
        self.manager = manager
        self.student = student
        self.ID = ID
        self.personal_address = personal_address
        self.credit = credit
        self.gpa = gpa

    def __str__(self):
        return f"School_address: {self.school_address}\nSchool: {self.school}\nDepartment: {self.department}\nManager: {self.manager}\nStudent: {self.student}\nID: {self.ID}\nPersonal_address: {self.personal_address}\nCredit: {self.credit}\nGPA: {self.gpa}"

    def set_school_address(self, adr):
        self.school_address = adr

    def get_school_address(self, adr):
        self.set_school_address(adr)

    def set_school(self, name):
        self.school = name

    def get_school(self, name):
        self.set_school(name)

    def set_department(self, dpm):
        self.department = dpm

    def get_deparment(self, dpm):
        self.set_department(dpm)

    def set_manager(self, dm):
        self.manager = dm

    def get_manager(self, dm):
        self.set_manager(dm)

    def set_student(self, name):
        self.student = name

    def get_student(self, name):
        self.set_student(name)

    def set_ID(self, id):
        self.ID = id

    def get_ID(self, id):
        self.set_ID(id)

    def set_personal_address(self, adr):
        self.personal_address = adr

    def get_personal_address(self, adr):
        self.set_personal_address(adr)

    def set_credit(self, cdt):
        self.credit = cdt

    def get_credit(self, cdt):
        self.set_credit(cdt)

    def set_GPA(self, sc):
        self.gpa = sc

    def get_GPA(self, sc):
        self.set_GPA(sc)


print("-----------Before edit-----------")
info = Student()
print(info)

print("-----------After edit-----------")

school_adr = "Tainan city yongkang district"
school = "STUST"
department = "CSE"
manager = "Gwo-Jiun Horng"
student = "Jason"
id = "4B0G0093"
personal_adr = "Tainan city yongkang district"
credit = "97"
gpa = "2.8"

info.get_school_address(school_adr)
info.get_school(school)
info.get_deparment(department)
info.get_manager(manager)
info.get_student(student)
info.get_ID(id)
info.get_personal_address(personal_adr)
info.get_credit(credit)
info.get_GPA(gpa)

print(info)
