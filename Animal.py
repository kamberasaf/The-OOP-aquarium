MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name: str, age: int, x: int, y: int, directionH: int) -> None:
        """
        Initialize an animal instance.
        :param name: Animal name
        :param age: Age in years
        :param x: X position in aquarium
        :param y: Y position in aquarium
        :param directionH: Horizontal direction (0=Left, 1=Right)
        """
        self.alive: bool = True
        self.width: int = MAX_ANIMAL_WIDTH
        self.height: int = MAX_ANIMAL_HEIGHT
        self.food: int = STARTING_FOOD
        self.name: str = name
        self.age: int = age
        self.x: int = x
        self.y: int = y
        self.directionH: int = directionH

    def __str__(self) -> str:
        """
        Return a string representation of the animal.
        """
        return (
            f"{self.name} (Age: {self.age}, Food: {self.food}, "
            f"Position: ({self.x}, {self.y}), DirectionH: {self.directionH}, "
            f"Alive: {self.alive})"
        )

    def get_food(self) -> int:
        return self.food

    def get_age(self) -> int:
        return self.age

    def dec_food(self) -> None:
        """
        Decrement food by one unit.
        If food reaches zero, the animal starves.
        """
        self.food -= 1
        if self.food <= 0:
            self.starvation()

    def inc_age(self) -> None:
        """
        Increment age by one.
        If age reaches MAX_AGE, the animal dies.
        """
        if not self.alive:
            return  # Dead animals don't age
        self.age += 1
        if self.age >= MAX_AGE:
            self.die()

    def right(self) -> None:
        """
        Move the animal one unit to the right.
        """
        self.set_x(self.x + 1)

    def left(self) -> None:
        """
        Move the animal one unit to the left.
        """
        self.set_x(self.x - 1)

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def starvation(self) -> None:
        """
        Handle starvation scenario.
        When animal starves, it dies.
        """
        print(f"{self.name} has starved to death.")
        self.die()

    def die(self) -> None:
        """
        Mark the animal as dead.
        """
        if self.alive:
            print(f"{self.name} has died.")
        self.alive = False

    def get_directionH(self) -> int:
        return self.directionH

    def set_directionH(self, directionH: int) -> None:
        self.directionH = directionH

    def get_alive(self) -> bool:
        return self.alive

    def get_size(self) -> tuple[int, int]:
        return self.height, self.width

    def get_food_amount(self) -> int:
        return self.food

    def add_food(self, amount: int) -> None:
        """
        Add food to the animal.
        """
        if amount > 0:
            self.food += amount

    def get_animal(self):
        """
        Return self. Could be overridden in subclasses if needed.
        """
        return self
