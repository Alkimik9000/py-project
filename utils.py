import os

def getNumberInRange(what_is_fetched: str = "Type input your input: ", error_to_display: str = "Your input", min_value: int = 0, max_value: int = 9999999999) -> int:
    while True:
        unverified_input = input(what_is_fetched + ": ")
        if not unverified_input.isdigit():
            print("Error: " + error_to_display + " must be a number. '" + unverified_input + "' is not a number")
            continue
        try:
            number_as_integer = int(unverified_input)
            if not (min_value <= number_as_integer <= max_value):
                print("Select a number between " + str(min_value) + " and " + str(max_value))
                continue
            return number_as_integer
        except ValueError:
            print("Error: Could not convert input to an integer.")


if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))
