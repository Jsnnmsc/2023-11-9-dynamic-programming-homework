import random


class Diamond:
    def __init__(self, carat, color, clarity, cut, price=0):
        self.carat = carat
        self.color = color
        self.clarity = clarity
        self.cut = cut
        self.price = price

    def __str__(self):
        return f"Carat: {self.carat}\nColor: {self.color}\nClarity: {self.clarity}\nCut: {self.cut}\nValue: {self.price}"

    def Price(self, start_at):
        self.price += (len(carats) - carats.index(self.carat) + 1) * 0.8
        +(len(colors) - colors.index(self.color) + 1) * 0.6
        +(len(clarities) - clarities.index(self.clarity) + 1) * 0.8
        +(len(cuts) - cuts.index(self.cut) + 1) * 0.4


carats = [2, 1, 0.5, 0.25]
colors = ["D", "G", "J", "M"]
clarities = ["FL", "VVS", "VS", "SI"]
cuts = ["EX", "VG", "G", "F", "P"]


d1 = Diamond(
    random.choice(carats),
    random.choice(colors),
    random.choice(clarities),
    random.choice(cuts),
)

d1.Price()
print(d1)
