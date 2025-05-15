from typing import List, Optional, Union

from crab import Crab
from fish import Fish
from moly import Moly
from ocypode import Ocypode
from scalar import Scalar
from shrimp import Shrimp

class AquaConstants:
    MAX_ANIMAL_HEIGHT = 8
    MAX_ANIMAL_WIDTH = 8
    MAX_CRAB_HEIGHT = 4
    MAX_CRAB_WIDTH = 7
    MAX_FISH_HEIGHT = 5
    MAX_FISH_WIDTH = 8
    WATERLINE = 3
    FEED_AMOUNT = 10
    MAX_AGE = 120

class Aqua:
    def __init__(self) -> None:
        self.animals: List[Union[Fish, Crab]] = []
        self.board: List[List[str]] = [
            [' '] * 30 for _ in range(12)
        ]
        self.print_board()

    def print_board(self) -> None:
        """
        Prints the aquarium board state.
        """
        for row in self.board:
            # Joining without spaces to avoid stretched visuals
            print(''.join(row))
        print("\n")

    def clear_board(self) -> None:
        """
        Clears the board for the next update.
        """
        self.board = [[' '] * 30 for _ in range(12)]

    def update_board(self) -> None:
        """
        Places all animals on the board according to their positions.
        """
        self.clear_board()
        for animal in self.animals:
            x, y = animal.position
            image = animal.get_image()
            height = len(image)
            width = len(image[0])
            for row in range(height):
                for col in range(width):
                    board_x = x + col
                    board_y = y + row
                    if 0 <= board_x < 30 and 0 <= board_y < 12:
                        pixel = image[row][col]
                        if pixel != ' ':
                            self.board[board_y][board_x] = pixel

    def check_if_free(self, x: int, y: int, height: int, width: int) -> bool:
        """
        Checks if a rectangular area is free of other animals on the board.
        """
        # Bounds check
        if x < 0 or y < 0 or x + width > 30 or y + height > 12:
            return False

        # Check for overlap with existing animals
        for animal in self.animals:
            ax, ay = animal.position
            a_height = animal.get_height()
            a_width = animal.get_width()

            if (x < ax + a_width and x + width > ax and
                y < ay + a_height and y + height > ay):
                # Overlapping rectangles -> space not free
                return False
        return True

    def add_fish(self, name: str, age: int, x: int, y: int, directionH: int,
                 directionV: int, fish_type: str) -> bool:
        """
        Adds a fish to the aquarium if space is free.
        """
        fish_class_map = {
            'sc': Scalar,
            'mo': Moly
        }
        fish_cls = fish_class_map.get(fish_type.lower())
        if not fish_cls:
            print(f"Unknown fish type: {fish_type}")
            return False

        fish = fish_cls(name, age, x, y, directionH, directionV)
        if not self.check_if_free(x, y, fish.get_height(), fish.get_width()):
            print(f"Position {x},{y} not free for fish {name}")
            return False

        self.animals.append(fish)
        return True

    def add_crab(self, name: str, age: int, x: int, y: int, directionH: int,
                 directionV: int, crab_type: str) -> bool:
        """
        Adds a crab to the aquarium if space is free.
        """
        crab_class_map = {
            'oc': Ocypode,
            'sh': Shrimp
        }
        crab_cls = crab_class_map.get(crab_type.lower())
        if not crab_cls:
            print(f"Unknown crab type: {crab_type}")
            return False

        crab = crab_cls(name, age, x, y, directionH, directionV)
        if not self.check_if_free(x, y, crab.get_height(), crab.get_width()):
            print(f"Position {x},{y} not free for crab {name}")
            return False

        self.animals.append(crab)
        return True

    def add_animal(self, name: str, age: int, x: int, y: int,
                   directionH: int, directionV: int, animal_type: str) -> bool:
        """
        Adds an animal of given type (fish or crab).
        """
        animal_type = animal_type.lower()
        add_methods = {
            'sc': self.add_fish,
            'mo': self.add_fish,
            'oc': self.add_crab,
            'sh': self.add_crab
        }
        method = add_methods.get(animal_type)
        if not method:
            print(f"Unknown animal type: {animal_type}")
            return False
        return method(name, age, x, y, directionH, directionV, animal_type)

    def is_collision(self) -> None:
        """
        Checks and resolves crab collisions by repositioning them randomly.
        """
        crabs = [a for a in self.animals if isinstance(a, Crab)]
        for i, crab1 in enumerate(crabs):
            for crab2 in crabs[i+1:]:
                if self._crabs_collide(crab1, crab2):
                    print(f"Collision detected between {crab1.name} and {crab2.name}")
                    self._resolve_crab_collision(crab1)
                    self._resolve_crab_collision(crab2)

    def _crabs_collide(self, crab1: Crab, crab2: Crab) -> bool:
        """
        Returns True if two crabs collide.
        """
        x1, y1 = crab1.position
        x2, y2 = crab2.position
        w1, h1 = crab1.get_width(), crab1.get_height()
        w2, h2 = crab2.get_width(), crab2.get_height()

        # Axis-Aligned Bounding Box collision detection
        if (x1 < x2 + w2 and x1 + w1 > x2 and
            y1 < y2 + h2 and y1 + h1 > y2):
            return True
        return False

    def _resolve_crab_collision(self, crab: Crab) -> None:
        """
        Repositions a crab randomly to resolve collision.
        """
        import random
        max_attempts = 10
        for _ in range(max_attempts):
            new_x = random.randint(0, 30 - crab.get_width())
            new_y = random.randint(AquaConstants.WATERLINE + 1,
                                   12 - crab.get_height())
            if self.check_if_free(new_x, new_y, crab.get_height(), crab.get_width()):
                crab.set_position(new_x, new_y)
                print(f"Crab {crab.name} moved to ({new_x},{new_y}) to resolve collision")
                return
        print(f"Failed to reposition crab {crab.name} after collision")

    # Movement methods for animals:
    def left(self, animal: Union[Fish, Crab]) -> None:
        """
        Moves the animal left if no collision or boundary.
        """
        x, y = animal.position
        if x <= 0:
            return  # boundary reached
        if self.check_if_free(x - 1, y, animal.get_height(), animal.get_width()):
            animal.set_position(x - 1, y)
            animal.set_direction_h(-1)

    def right(self, animal: Union[Fish, Crab]) -> None:
        """
        Moves the animal right if no collision or boundary.
        """
        x, y = animal.position
        max_width = AquaConstants.MAX_CRAB_WIDTH if isinstance(animal, Crab) else AquaConstants.MAX_FISH_WIDTH
        if x + max_width >= 30:
            return  # boundary reached
        if self.check_if_free(x + 1, y, animal.get_height(), animal.get_width()):
            animal.set_position(x + 1, y)
            animal.set_direction_h(1)

    def up(self, animal: Union[Fish, Crab]) -> None:
        """
        Moves the animal up if no collision or boundary.
        """
        x, y = animal.position
        if y <= AquaConstants.WATERLINE:
            return  # water surface reached
        if self.check_if_free(x, y - 1, animal.get_height(), animal.get_width()):
            animal.set_position(x, y - 1)
            animal.set_direction_v(-1)

    def down(self, animal: Union[Fish, Crab]) -> None:
        """
        Moves the animal down if no collision or boundary.
        """
        x, y = animal.position
        max_height = AquaConstants.MAX_CRAB_HEIGHT if isinstance(animal, Crab) else AquaConstants.MAX_FISH_HEIGHT
        if y + max_height >= 12:
            return  # bottom reached
        if self.check_if_free(x, y + 1, animal.get_height(), animal.get_width()):
            animal.set_position(x, y + 1)
            animal.set_direction_v(1)

    def feed(self) -> None:
        """
        Feeds all animals, increasing their age and possibly affecting behavior.
        """
        for animal in self.animals:
            animal.increase_age(AquaConstants.FEED_AMOUNT)
            if animal.get_age() > AquaConstants.MAX_AGE:
                print(f"{animal.name} reached max age and is removed.")
                self.animals.remove(animal)
