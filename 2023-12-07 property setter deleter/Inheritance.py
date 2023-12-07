class Sports:
    def __init__(self, name=None):
        self._name = name

    @property
    def sport_name(self):
        return self._name

    @sport_name.setter
    def sport_name(self, value):
        self._name = value


class Land_sport(Sports):
    def __init__(self, name=None, field=None):
        super().__init__(name)
        self._field = field

    @property
    def Land_sport_field(self):
        return self._field


class Water_sport(Sports):
    def __init__(self, name=None, field=None):
        super().__init__(name)
        self._field = field

    @property
    def Water_sport_field(self):
        return self._field


sport1 = Land_sport()
sport1._name = "baseball"
sport1._field = "baseball field"

sport2 = Water_sport()
sport2._name = "swimming"
sport2._field = "pool"

print(f"Land sport: {sport1._name}, {sport1._field}")
print(f"Water sport: {sport2._name}, {sport2._field}")
