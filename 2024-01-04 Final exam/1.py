class fried_chicken:
    # 初始化產地、風味、醬汁、辣度、部位
    def __init__(self, origin=None, flavor=None, sauce=None, spicy=None, meat=None):
        self.origin = origin
        self.flavor = flavor
        self.sauce = sauce
        self.spicy = spicy
        self.meat = meat

    def __str__(self):
        return f"Origin:{self.origin}  Meat:{self.meat}  Flavor:{self.flavor}  Sauce:{self.sauce}  Spicy:{self.spicy}\n"

    # 選擇產地
    def chicken_origin(self):
        ori = int(
            input("Option 1: Taiwan, Option 2: USA\nChoose your flavor(Enter 1 or 2):")
        )
        if ori == 1:
            self.origin = "Taiwan"
        else:
            self.origin = "USA"

    # 選擇部位(雞胸、雞腿)
    def chicken_meat(self):
        mt = int(
            input(
                "Option 1: White meat, Option 2: Dark meat\nChoose your chicken meat part(Enter 1 or 2):"
            )
        )
        if mt == 1:
            self.meat = "White meat"
        else:
            self.meat = "Dark meat"

    def chicken_all_flavor(self):
        # 選擇風味
        flav = int(
            input(
                "Option 1: Rosemary, Option 2: Pepper\nChoose your flavor(Enter 1 or 2):"
            )
        )
        if flav == 1:
            self.flavor = "Rosemary"
        else:
            self.flavor = "Pepper"

        # 選擇醬料
        sau = int(
            input(
                "Option 1: Korean fried chicken sauce, Option 2: Honey sauce\nChoose your sauce(Enter 1 or 2):"
            )
        )
        if sau == 1:
            self.sauce = "Korean fried chicken sauce"
        else:
            self.sauce = "Honey sauce"

        # 選擇辣度
        spi = int(
            input(
                "Option 1: None spicy, Option 2: Little spicy\nChoose your spicy(Enter 1 or 2):"
            )
        )
        if spi == 1:
            self.spicy = "None spicy"
        else:
            self.spicy = "Little spicy"


# 宣告物件
fried_chicken_1 = fried_chicken()
fried_chicken_2 = fried_chicken()
fried_chicken_3 = fried_chicken()
fried_chicken_4 = fried_chicken()

# 以下自行輸入測試
fried_chicken_1.chicken_origin()
fried_chicken_1.chicken_meat()
fried_chicken_1.chicken_all_flavor()
print(fried_chicken_1)

fried_chicken_2.chicken_origin()
fried_chicken_2.chicken_meat()
fried_chicken_2.chicken_all_flavor()
print(fried_chicken_2)

fried_chicken_3.chicken_origin()
fried_chicken_3.chicken_meat()
fried_chicken_3.chicken_all_flavor()
print(fried_chicken_3)

fried_chicken_4.chicken_origin()
fried_chicken_4.chicken_meat()
fried_chicken_4.chicken_all_flavor()
print(fried_chicken_4)
