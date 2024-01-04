class employer:
    # 初始化員工資訊 名稱、年資、工作時數
    def __init__(self, name, seniority, worktime):
        self.name = name
        self.seniority = seniority
        self.worktime = worktime
        self.month_salary = None  # 月薪
        self.salary_per_hour = 200  # 時薪

    # 查詢員工名子
    def check_name(self):
        return f"Employee name:{self.name}"

    # 查詢員工年資
    def check_seniority(self):
        return f"Employee seniority:{self.seniority}"

    # 查詢員工工作時數
    def check_worktime(self):
        return f"Employee worktime:{self.worktime}"

    # 查詢員工月薪
    def check_month_salary(self):
        self.month_salary = self.salary_per_hour * self.worktime
        return f"Month salary:{self.month_salary}"

    # 增加工作時數
    def increase_worktime(self):
        add = int(input("Increase work time amount:"))
        self.worktime += add
        return f"Worktime now:{self.worktime}"

    # 增加年資
    def increase_seniority(self):
        add = int(input("Increase seniority amount:"))
        self.seniority += add
        return f"Seniority now:{self.seniority}"


class cold_drinks:
    def __init__(self, c_name, ice, c_sweet):
        self.c_name = c_name
        self.ice = ice
        self.c_sweet = c_sweet


class hot_drinks:
    def __init__(self, h_name, h_sweet):
        self.h_name = h_name
        self.h_sweet = h_sweet


class STUST_CSIE_DRINKS_STORE(employer, cold_drinks, hot_drinks):
    def __init__(self, name, seniority, worktime):
        super().__init__(name, seniority, worktime)


cold_drink1 = cold_drinks("Ice tea", "half ice", "half sweet")
cold_drink2 = cold_drinks("Black tea", "full ice", "none sweet")
cold_drink3 = cold_drinks("Green Tea", "half ice", "none sweet")

hot_drinks1 = hot_drinks("Green tea", "none sweet")
hot_drinks2 = hot_drinks("Black tea", "half sweet")
hot_drinks3 = hot_drinks("Woolong tea", "none sweet")


emp_1 = STUST_CSIE_DRINKS_STORE("Jason", 10, 40)
print(emp_1.check_name())
print(emp_1.check_seniority())
print(emp_1.check_worktime())
print(emp_1.check_month_salary())
print(emp_1.increase_seniority())
print(emp_1.increase_worktime())
