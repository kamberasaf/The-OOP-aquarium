from Animal import Animal

MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8

class Fish(Animal):
    """
    Fish class represents a fish animal in the aquarium.
    Inherits from Animal.
    """

    def __init__(self, name: str, age: int, x: int, y: int, directionH: int, directionV: int) -> None:
        """
        Initializes a Fish instance.

        Parameters:
            name (str): Fish's name.
            age (int): Fish's age.
            x (int): Horizontal position.
            y (int): Vertical position.
            directionH (int): Horizontal direction (-1 left, 1 right).
            directionV (int): Vertical direction (-1 up, 1 down).
        """
        super().__init__(name, age, x, y, directionH)
        self._directionV = directionV

    def __str__(self) -> str:
        """
        Returns a string representation of the fish.
        """
        return f"The fish {self.name} is {self.age} years old and has {self.food} food"

    def up(self) -> None:
        """Moves the fish up by decreasing the y coordinate."""
        self.set_y(self.y - 1)

    def down(self) -> None:
        """Moves the fish down by increasing the y coordinate."""
        self.set_y(self.y + 1)

    def starvation(self) -> None:
        """
        Called when fish runs out of food, killing it.
        """
        print(f"The fish {self.name} died at the age of {self.age} years because it ran out of food!")
        self.alive = False

    def die(self) -> None:
        """Kills the fish in good health."""
        self.alive = False

    @property
    def directionV(self) -> int:
        """Vertical direction getter."""
        return self._directionV

    @directionV.setter
    def directionV(self, value: int) -> None:
        """Vertical direction setter."""
        self._directionV = value

    @property
    def height(self) -> int:
        """Returns fish's height."""
        return MAX_FISH_HEIGHT

    @property
    def width(self) -> int:
        """Returns fish's width."""
        return MAX_FISH_WIDTH
