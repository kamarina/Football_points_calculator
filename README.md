# Football Points Calculator

This Python program calculates the total points for a football team based on the number of wins, draws, and losses. It utilizes a simple scoring system where wins contribute 3 points, draws contribute 1 point, and losses contribute 0 points.

## How to Use

1. Run the program by executing the Python script (`football_points_calculator.py`).
2. Enter the number of wins, draws, and losses when prompted.
3. The program will calculate and display the total points for the football team.

## Program Components

### `football_points(wins, draws, losses)`

This function takes the number of wins, draws, and losses as arguments and calculates the total points using the specified scoring system.

### `get_input(prompt)`

This function prompts the user to enter a positive integer value. It ensures that the entered value is greater than 0 and handles invalid non-numerical input.

## Example

```python
# Example usage of the program
wins = get_input("Please enter number of wins: ")
draws = get_input("Please enter number of draws: ")
losses = get_input("Please enter number of losses: ")

total_points = football_points(wins, draws, losses)
print(f"Total points: {total_points} points.")
