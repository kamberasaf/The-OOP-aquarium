# ocypode.py
from crab import Crab


class Ocypode(Crab):
    def __init__(self, name, age, x, y, direction_h):
        super().__init__(name, age, x, y, direction_h)
        self.width = 7
        self.height = 4

    def get_animal(self):
        ocypode = [
            ' *   * ',
            '  ***  ',
            '*******',
            '*     *'
        ]
        return ocypode
