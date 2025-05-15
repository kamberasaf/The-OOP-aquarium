from Crab import Crab


class Shrimp(Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def get_animal(self):
        shrimp = [
            '    * *',
            '****** ',
            '  * *  '
        ]

        if self.directionH == 0:
            shrimp = [line[::-1] for line in shrimp]

        return shrimp
