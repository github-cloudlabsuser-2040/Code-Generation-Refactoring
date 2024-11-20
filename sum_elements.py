#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases
#refactor the code to make it more readable and maintainable.
#The code should be broken down into smaller functions, and each function should have a single responsibility.
#The code should handle exceptions and provide meaningful error messages to the user.
#The code should be well-documented and easy to understand.
#The code should follow the PEP 8 style guide for Python code.

MAX = 100

def validate_input(arr):
    if not isinstance(arr, list):
        raise ValueError("Input should be a list.")
    if not all(isinstance(num, (int, float)) for num in arr):
        raise ValueError("All elements in the list should be numbers.")
    if len(arr) > MAX:
        raise ValueError(f"List should not contain more than {MAX} elements.")

def calculate_sum(arr):
    validate_input(arr)
    return sum(arr)

def main():
    try:
        arr = [1, 2, 3, 4, 5]  # Example input
        total = calculate_sum(arr)
        print(f"The sum of the elements is: {total}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()