def func(a, b):
    def add():
        return a + b

    sum = add()

    return sum + 5


print(func(1, 2))
