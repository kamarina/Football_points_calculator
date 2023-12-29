# Function to calculate the total points for a football team
def football_points(wins, draws, losses):
    # Calculate total points based on the given rules
    total_points = (wins * 3) + (draws * 1) + (losses * 0)
    return total_points


# Function to get a positive integer input from the user
def get_input(prompt):
    while True:
        try:
            # Attempt to convert user input to an integer
            value = int(input(prompt))

            # Check if the entered value is greater than 0
            if value > 0:
                return value
            else:
                # Print an error message if the input is less than 0
                print("Invalid input, value must be greater than 0.")
        except ValueError:
            # Print an error message if the input is not a valid integer
            print("Invalid input. Please enter a valid numeric value.")


# Get positive inputs for the number of wins, draws, and losses
wins = get_input("Please enter number of wins: ")
draws = get_input("Please enter number of draws: ")
losses = get_input("Please enter number of losses: ")

# Calculate and print the total points for the football team
total_points = football_points(wins, draws, losses)
print(f"Total points: {total_points} points.")
