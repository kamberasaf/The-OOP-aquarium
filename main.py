import time
from typing import Optional

import Aqua


def parse_positive_int(value: str, min_value: int = 1, max_value: Optional[int] = None) -> Optional[int]:
    """
    Parse string input to a positive integer between min_value and max_value.
    Return None if invalid.
    """
    try:
        num = float(value)
        if not num.is_integer():
            return None
        num = int(num)
        if num < min_value:
            return None
        if max_value is not None and num > max_value:
            return None
        return num
    except ValueError:
        return None


def input_choice(prompt: str, valid_choices: list[int]) -> int:
    """Prompt user to input one of valid_choices, repeat until valid."""
    while True:
        choice = input(prompt)
        parsed = parse_positive_int(choice)
        if parsed in valid_choices:
            return parsed
        print(f"Please enter a valid number: {valid_choices}")


def input_direction(prompt: str) -> int:
    """Prompt user for direction input (0 or 1)."""
    while True:
        val = input(prompt)
        parsed = parse_positive_int(val, 0, 1)
        if parsed in [0, 1]:
            return parsed
        print("Please enter 0 or 1.")


def input_name(prompt: str) -> str:
    """Prompt user for a valid name with only alphanumeric characters or spaces."""
    while True:
        name = input(prompt).strip()
        if name and all(c.isalnum() or c == ' ' for c in name):
            return name
        print("Please enter a valid name (letters, numbers, and spaces only).")


def input_animal_position(prompt_x: str, prompt_y: str, aqua: Aqua.Aqua, fish_type: int) -> tuple[int, int]:
    """
    Prompt for animal position.
    X must be between 1 and aqua_width-1.
    Y depends on animal type; fish (1,2) in waterline to height-1, others Y=0.
    """
    max_x = aqua.aqua_width - 1
    while True:
        x = parse_positive_int(input(prompt_x), 1, max_x)
        if x is None:
            print(f"Please enter an integer between 1 and {max_x}.")
            continue
        break

    y = 0
    if fish_type in [1, 2]:  # fish need Y input
        min_y = Aqua.WATERLINE
        max_y = aqua.aqua_height - 1
        while True:
            y_val = parse_positive_int(input(prompt_y), min_y, max_y)
            if y_val is None:
                print(f"Please enter an integer between {min_y} and {max_y}.")
                continue
            y = y_val
            break
    return x, y


def demo(myaqua: Aqua.Aqua, sleep_time: float = 0.5) -> None:
    """Run a demo with preset animals and aquarium simulation."""
    myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh')
    myaqua.add_animal("ocypodcrab1", 13, 41, myaqua.aqua_height, 0, 0, 'oc')
    myaqua.print_board()

    for i in range(120):
        if i % 50 == 0:
            myaqua.feed_all()
        myaqua.next_turn()
        if i != 119:
            myaqua.print_board()
            print('\n')
        time.sleep(sleep_time)


def add_animal(myaqua: Aqua.Aqua) -> None:
    """Interactively add an animal to the aquarium."""
    print("\nPlease select an animal type:")
    print("1. Scalar")
    print("2. Moly")
    print("3. Ocypode")
    print("4. Shrimp")

    fish_type = input_choice("What animal do you want to put in the aquarium? ", [1, 2, 3, 4])
    name = input_name("Please enter a name: ")
    age = input_choice("Please enter age (1-100): ", list(range(1, 101)))

    x, y = input_animal_position(
        f"Please enter an X axis location (1 - {myaqua.aqua_width - 1}): ",
        f"Please enter a Y axis location ({Aqua.WATERLINE} - {myaqua.aqua_height - 1}): ",
        myaqua,
        fish_type,
    )

    directionH = input_direction("Please enter horizontal direction (0 for Left, 1 for Right): ")

    # Vertical direction only for fish (1 and 2)
    directionV = 0
    if fish_type in [1, 2]:
        directionV = input_direction("Please enter vertical direction (0 for Down, 1 for Up): ")

    type_map = {1: 'sc', 2: 'mo', 3: 'oc', 4: 'sh'}
    success = myaqua.add_animal(name, age, x, y, directionH, directionV, type_map[fish_type])

    if not success:
        print("Failed to add animal. Please try different parameters.")


def print_main_menu() -> None:
    print("\nMain menu\n" + "-" * 30)
    print("1. Add an animal")
    print("2. Drop food into the aquarium")
    print("3. Take a step forward")
    print("4. Take several steps")
    print("5. Demo")
    print("6. Print all")
    print("7. Exit")


def main() -> None:
    print('\nWelcome to "The OOP Aquarium"')

    width = input_choice("The width of the aquarium (Minimum 40): ", list(range(40, 10000)))
    height = input_choice("The height of the aquarium (Minimum 25): ", list(range(25, 10000)))

    myaqua = Aqua.Aqua(width, height)

    while True:
        print_main_menu()
        choice = input_choice("What do you want to do? ", list(range(1, 8)))

        if choice == 1:
            add_animal(myaqua)
        elif choice == 2:
            myaqua.feed_all()
        elif choice == 3:
            myaqua.next_turn()
        elif choice == 4:
            myaqua.several_steps()
        elif choice == 5:
            demo(myaqua)
        elif choice == 6:
            myaqua.print_all()
        else:  # Exit
            print("Bye bye")
            break

        myaqua.print_board()
        print('\n')


if __name__ == "__main__":
    main()
