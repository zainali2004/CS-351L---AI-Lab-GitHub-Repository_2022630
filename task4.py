def bfs_systematic_number_guessing_game():
    # Introduce the game
    print("Think of a number between 1 to 100, and AI will try to guess it.")

    low = 1
    high = 100
    attempts = 0
    max_attempts = 10  # Maximum number of attempts

    # Loop until the correct guess or until max attempts are reached
    while attempts < max_attempts and low <= high:
        current_guess = (low + high) // 2  # Systematically guess the midpoint of the current range
        attempts += 1

        print(f"AI's guess is: {current_guess} (Attempt {attempts}/{max_attempts})")

        # Get feedback from the player
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"AI guessed the correct number in {attempts} attempts!")
            return
        elif feedback == 'h':
            high = current_guess - 1  # Adjust the upper bound
        elif feedback == 'l':
            low = current_guess + 1  # Adjust the lower bound
        else:
            # Handle invalid input
            print("Something went wrong! Invalid input.")
            return

    # If max attempts are reached and the correct number wasn't guessed
    if attempts >= max_attempts:
        print(f"AI couldn't guess the number within {max_attempts} attempts.")
    else:
        print("Something went wrong!")

# Run the BFS systematic guessing game
bfs_systematic_number_guessing_game()