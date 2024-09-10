import random

def dfs_number_guessing_game():

  # AI guesses a number
  print("think of a number between 1 to 100 and AI will guess it")
  low = 1
  high = 100
  attempts = 0
  max_attempts = 10
  # Start the guessing from 50
  #current_guess = 50

# loop goes on until it guesses the correct number
  while low <= high and attempts < max_attempts:
    current_guess = random.randint(low, high)

    attempts += 1
    print(f"Ai guess is: {current_guess}")

    feedback = input("enter h if too high, enter l if too low, enter c if correct")

    if feedback == "c":
      print(f"Ai guessed the correct number in {attempts} attempts") #if the number is guessed correctly
      return

    elif feedback == "h":
      high = current_guess - 1 # if too high, adjust upper bound
    elif feedback == "l":
      low = current_guess + 1 # if too low, adjust lower bound

    else:
        # If the input is not 'h', 'l', or 'c', show an error and break the loop
        print("Something went wrong! Invalid input.")
        return  # Exit the game if invalid input is detected

# exits the loop without finding the correct number
  if attempts >= max_attempts:
      print(f"AI couldn't guess the number within {max_attempts} attempts.")
  else:
      print("Something went wrong!")

# to run the code
dfs_number_guessing_game()