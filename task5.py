import random

# Define the golden ratio
GOLDEN_RATIO = (1 + 5 ** 0.5) / 2

def golden_ratio_number_guessing_game():
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")

    low = 1
    high = 100
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts and low <= high:
        # Calculate the two points within the range based on the golden ratio
        range_size = high - low
        middle1 = high - int(range_size / GOLDEN_RATIO)
        middle2 = low + int(range_size / GOLDEN_RATIO)

        # AI chooses one of the two points randomly
        current_guess = random.choice([middle1, middle2])

        attempts += 1
        print(f"AI's guess is: {current_guess} (Attempt {attempts}/{max_attempts})")

        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"AI guessed your number in {attempts} attempts!")
            return
        elif feedback == 'h':
            high = current_guess - 1  # Adjust the upper bound if guess is too high
        elif feedback == 'l':
            low = current_guess + 1  # Adjust the lower bound if guess is too low
        else:
            print("Something went wrong! Invalid input.")
            return

    # If AI couldn't guess within the max number of attempts
    if attempts >= max_attempts:
        print(f"AI couldn't guess your number within {max_attempts} attempts.")

# Run the Golden Ratio version of the game
golden_ratio_number_guessing_game()