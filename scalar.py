# scalar.py
from fish import Fish


class Scalar(Fish):
    def __init__(self, name, age, x, y, direction_h, direction_v):
        super().__init__(name, age, x, y, direction_h, direction_v)
        self.width = 8
        self.height = 5

    def get_animal(self):
        scalar = [
            '******  ',
            '    *** ',
            '  ******',
            '    *** ',
            '******  '
        ]

        if self.direction_h == 0:  # scalar looking left, reverse each line
            scalar = [line[::-1] for line in scalar]

        return scalar
