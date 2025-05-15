MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH

    def __str__(self):
        pass

    def get_food(self) -> int:
        return self.food

    def get_age(self) -> int:
        return self.age

    def dec_food(self):
        self.food -= 1
        if self.food == 0:
            self.starvation()

    def inc_age(self):
        if not self.get_alive():
            return None  # we won't feed a dead fish.
        self.age += 1
        if self.age == 120:
            self.die()

    def right(self):
        self.set_x(self.x + 1)

    def left(self):
        self.set_x(self.x - 1)

    def get_position(self) -> (int, int):
        return self.x, self.y

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y):
        self.y = y

    def starvation(self):
        pass

    def die(self):
        pass

    def get_directionH(self) -> int:
        return self.directionH

    def set_directionH(self, directionH):
        self.directionH = directionH

    def get_alive(self) -> bool:
        return self.alive

    def get_size(self) -> (int, int):
        return self.height, self.width

    def get_food_amount(self) -> int:
        return self.food

    def add_food(self, amount: int):
        self.food += amount

    def get_animal(self):
        pass
