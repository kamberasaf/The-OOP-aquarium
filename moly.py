# moly.py
from fish import Fish


class Moly(Fish):
    def __init__(self, name, age, x, y, direction_h, direction_v):
        super().__init__(name, age, x, y, direction_h, direction_v)
        self.width = 8
        self.height = 3

    def get_animal(self):
        moly = [
            '*   *** ',
            '********',
            '*   *** '
        ]

        if self.direction_h == 0:  # facing left, reverse each line
            moly = [line[::-1] for line in moly]

        return moly
