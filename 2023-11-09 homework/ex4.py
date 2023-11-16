def show_employee(*args):
    if len(args) > 1:
        print(f"Name: {args[0]}, Salary: {args[1]}")
    else:
        print(f"Name: {args[0]}, Salary: 9000")


show_employee("Ben", 12000)
show_employee("Jessa")
