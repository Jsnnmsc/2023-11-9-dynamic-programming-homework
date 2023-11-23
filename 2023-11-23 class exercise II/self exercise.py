import random


class Diamond:
    def __init__(self, carat, color, clarity, cut):
        self.carat = carat
        self.color = color
        self.clarity = clarity
        self.cut = cut

    def __str__(self):
        print(
            f"Carat: {self.carat}\nColor: {self.color}\nClarity: {self.clarity}\nCut: {self.cut}"
        )

    def Price(self):
        pass


carats = [0.25, 0.5, 1, 2]
colors = ["D", "G", "J", "M"]
clarities = ["FL", "VVS", "VS", "SI"]
cuts = ["EX", "VG", "G", "F", "P"]

d1 = Diamond(
    random.choice(carats),
    random.choice(colors),
    random.choice(clarities),
    random.choice(cuts),
)
print(d1)
