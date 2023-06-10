mofde
September 12, 2019
The computer will think of a secret number from 1 to 10 and ask the user to guess it. After each guess, the computer will tell the user whether the number is too high or too low. The user wins if they can guess the number within whatever the computer’s number is.
I decided to give only ten attempts to guess because it would be more interesting if there was a tie or draw. However, it would be a rare case for smart players. Ten tries would be a great number because the maximum is ten.

'''

# Import the randint function generate random integers from random import randint

# Establish the lower an uppper bound on the goal number
MINIMUM = 1
MAXIMUM = 10
numberOfTries = 0
def print_welcome():
    '''

    Prompt the user for their name, and then display a simple message explaining the rules of the game
    '''

    # Get the name of the user
    name = input("What is your name?")
    # Show the user's name
    print("Hello", name, "and welcome to my guessing game.")
    # Print out the limits of the goal number
    print("I've thought of a number between", MINIMUM, "and", MAXIMUM)
    # Write out rest of the instructions
    print("You need to guess that number.")
    print("I'll tell you if you need to go higher or lower.")
    
def print_ending():
    '''
    Print out a conclusive message to wrap up the game.
    '''
    print("You win!")

def process_guess(guess, goal):
        Print out whether or not the user was above, below, or at the goal.
        
        Args:
            guess (int): The number that the user entered as their guess.
            goal (int): The number that the computer is thinking of.
        '''
        # Branch execution based on whether the guess was right
        if guess < goal:
            print("You need to go higher!")
        elif guess > goal:
            print("You need to go lower!")
        else:
            print("That's correct, it's", goal)
            
        if numberOfTries = 10;
            print("Game Over");
            
    def get_number():
        '''
        Ask the user for a number, and keep prompting them until they give you an actual number (as opposed to giving you a letter).
        '''
        # Get the guess from the user, returns a string number = input("What is your guess?")
        # Was the string composed only of numbers?
        if number.isdigit():
            # If so, we can safely convert it to an integer
            number_as_int = int(number)
            # And return the result
            return number_as_int
        else:
            # Otherwise, call this function again recursively
            return get_number()
        
    def main_game():
        '''
        Play a round of the game.
        '''
        #Pick random number between MINIMUM and MAXIMUM
        goal = randint(MINIMUM, MAXIMUM)

# Initially, the user hasn't guessed anything.
        user_guess = None
        
        print_welcom()
        # Repeatedly ask the user until they get it right while user_guess !- goal:
            user_guess = get_number()
            process_guess(user_guess, goal)
        print_ending()
        
        # This if statement is commin in most professional Python
        #   programs - don't worry too much about what it does.
        #   but you can safely assume it will work when you press
        #   the run button.
        if _name_ == '_main_':
            main_game()