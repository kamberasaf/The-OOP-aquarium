from Animal import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7

class Crab(Animal):
    """
    Crab class represents a crab animal in the aquarium.
    Inherits from Animal.
    """

    def __init__(self, name: str, age: int, x: int, y: int, directionH: int) -> None:
        """
        Initializes a Crab instance.
        
        Parameters:
            name (str): Crab's name.
            age (int): Crab's age.
            x (int): Horizontal position.
            y (int): Vertical position.
            directionH (int): Horizontal direction (-1 left, 1 right).
        """
        super().__init__(name, age, x, y, directionH)

    def __str__(self) -> str:
        """
        Returns a string representation of the crab.
        """
        return f"The crab {self.name} is {self.age} years old and has {self.food} food"

    def starvation(self) -> None:
        """
        Called when crab runs out of food, killing it.
        """
        self.alive = False
        print(f"The crab {self.name} died at the age of {self.age} years because it ran out of food!")

    def die(self) -> None:
        """
        Called when crab dies in good health.
        """
        self.alive = False
        print(f"{self.name} died in good health.")

    @property
    def height(self) -> int:
        """Returns crab's height (used for collision and board placement)."""
        return MAX_CRAB_HEIGHT

    @property
    def width(self) -> int:
        """Returns crab's width (used for collision and board placement)."""
        return MAX_CRAB_WIDTH

