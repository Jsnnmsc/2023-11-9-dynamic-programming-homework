def display_student(name, age):
    def show_student(new_name, new_age):
        print(new_name, new_age)

    show_student(name, age)


display_student("Emma", 26)
